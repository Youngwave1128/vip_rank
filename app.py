# app.py
from flask import Flask, render_template, request, redirect, Response
import json
import threading
import time

app = Flask(__name__, static_folder='static')

# SSE 클라이언트들을 저장할 리스트
sse_clients = []

# 1~17번 테이블 초기화
tables = {i: 0 for i in range(1, 18)}

@app.route("/")
def index():
    # 가격 기준 내림차순, 같으면 테이블 번호 오름차순
    # 가격이 0이 아닌 테이블만 필터링
    filtered_tables = {k: v for k, v in tables.items() if v > 0}
    sorted_tables = sorted(filtered_tables.items(), key=lambda x: (-x[1], x[0]))
    top5 = sorted_tables[:5]
    return render_template("index.html", top5=top5)

@app.route("/admin")
def admin():
    # 가격이 0이 아닌 테이블만 필터링해서 현재 현황 표시
    filtered_tables = {k: v for k, v in tables.items() if v > 0}
    sorted_tables = sorted(filtered_tables.items(), key=lambda x: (-x[1], x[0]))
    return render_template("admin.html", tables=dict(sorted_tables))

@app.route("/update", methods=["POST"])
def update():
    table_num = int(request.form["table"])
    price = int(request.form["price"])
    tables[table_num] += price  # 기존 가격에 더하기
    
    # 모든 SSE 클라이언트에게 업데이트 알림 전송
    for client in sse_clients:
        try:
            client.put("data: update\n\n")
        except:
            pass
    
    return redirect("/admin")

@app.route("/reset", methods=["POST"])
def reset():
    global tables
    tables = {i: 0 for i in range(1, 18)}  # 모든 테이블 초기화
    
    # 모든 SSE 클라이언트에게 업데이트 알림 전송
    for client in sse_clients:
        try:
            client.put("data: update\n\n")
        except:
            pass
    
    return redirect("/admin")

@app.route("/events")
def events():
    def event_stream():
        # 큐를 생성하고 클라이언트 리스트에 추가
        import queue
        client_queue = queue.Queue()
        sse_clients.append(client_queue)
        
        try:
            while True:
                # 큐에서 메시지 대기
                msg = client_queue.get()
                yield msg
        except GeneratorExit:
            # 클라이언트가 연결을 끊으면 리스트에서 제거
            sse_clients.remove(client_queue)
    
    return Response(event_stream(), mimetype='text/event-stream')
    
if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
