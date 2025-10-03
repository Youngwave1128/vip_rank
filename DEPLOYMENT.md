# 배포 가이드

## 🚀 빠른 배포 방법

### 1. Railway 배포 (추천)

1. **Railway 계정 생성**
   - https://railway.app 접속
   - GitHub 계정으로 로그인

2. **프로젝트 연결**
   - "New Project" 클릭
   - "Deploy from GitHub repo" 선택
   - 이 저장소 선택

3. **자동 배포**
   - Railway가 자동으로 감지하고 배포
   - 배포 완료 후 URL 확인

### 2. Render 배포

1. **Render 계정 생성**
   - https://render.com 접속
   - GitHub 계정으로 로그인

2. **웹 서비스 생성**
   - "New +" → "Web Service" 선택
   - GitHub 저장소 연결
   - 설정:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `python app.py`

3. **배포**
   - "Create Web Service" 클릭
   - 자동 배포 완료

### 3. Heroku 배포

1. **Heroku CLI 설치**
   ```bash
   # macOS
   brew install heroku/brew/heroku
   
   # Windows
   # https://devcenter.heroku.com/articles/heroku-cli 다운로드
   ```

2. **Heroku 로그인**
   ```bash
   heroku login
   ```

3. **앱 생성 및 배포**
   ```bash
   heroku create your-app-name
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

### 4. PythonAnywhere 배포

1. **PythonAnywhere 계정 생성**
   - https://www.pythonanywhere.com 접속

2. **파일 업로드**
   - Files 탭에서 프로젝트 파일들 업로드

3. **WSGI 설정**
   - Web 탭에서 WSGI 설정 파일 수정:
   ```python
   import sys
   path = '/home/yourusername/yourproject'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```

## 🔧 배포 후 설정

### 환경 변수 (선택사항)
- `DEBUG=False`: 프로덕션 모드
- `PORT=5000`: 포트 설정

### 도메인 연결 (선택사항)
- Railway, Render, Heroku 모두 커스텀 도메인 지원
- DNS 설정에서 CNAME 레코드 추가

## 📱 사용법

1. **메인 페이지**: 실시간 순위 확인
2. **관리자 페이지**: `/admin` 경로로 접속하여 테이블 관리
3. **실시간 업데이트**: 자동으로 순위 반영

## 🛠️ 문제 해결

### 일반적인 문제들

1. **배포 실패**
   - `requirements.txt` 파일 확인
   - Python 버전 호환성 확인

2. **정적 파일 로드 안됨**
   - `static/` 폴더 경로 확인
   - 파일명 대소문자 확인

3. **실시간 업데이트 안됨**
   - 브라우저 캐시 삭제
   - SSE 연결 상태 확인

### 로그 확인
- Railway: Dashboard → Deployments → Logs
- Render: Dashboard → Logs
- Heroku: `heroku logs --tail`

## 💡 팁

- **무료 플랜**: Railway, Render 모두 무료 플랜 제공
- **자동 배포**: GitHub에 푸시하면 자동 배포
- **환경 변수**: 민감한 정보는 환경 변수로 관리
- **백업**: 정기적으로 데이터 백업 권장
