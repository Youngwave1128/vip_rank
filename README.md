# VIP RANK - 실시간 순위 시스템

VIP 테이블들의 실시간 순위를 표시하는 웹 애플리케이션입니다.

## 기능

- 🏆 **실시간 순위 표시**: 상위 5개 테이블의 실시간 순위
- 🥇 **상위 3등 강조**: 금색(1등), 은색(2등), 동색(3등) 글로우 효과
- 📊 **관리자 페이지**: 테이블별 금액 입력 및 관리
- 🔄 **실시간 업데이트**: Server-Sent Events로 자동 새로고침
- 📱 **반응형 디자인**: 전체화면 최적화

## 설치 및 실행

### 로컬 실행

1. 저장소 클론
```bash
git clone <repository-url>
cd vip-rank
```

2. 의존성 설치
```bash
pip install -r requirements.txt
```

3. 애플리케이션 실행
```bash
python app.py
```

4. 브라우저에서 접속
- 메인 페이지: `http://localhost:5000`
- 관리자 페이지: `http://localhost:5000/admin`

### 환경 변수

- `PORT`: 포트 번호 (기본값: 5000)
- `DEBUG`: 디버그 모드 (기본값: False)

## 사용법

### 관리자 페이지
1. `/admin` 경로로 접속
2. 테이블 번호와 금액 입력
3. "업데이트" 버튼 클릭
4. 메인 페이지에서 실시간 순위 확인

### 메인 페이지
- 상위 5개 테이블의 실시간 순위 표시
- 상위 3등은 각각 금색, 은색, 동색으로 강조
- 파인애플 로고 클릭 시 관리자 페이지로 이동

## 기술 스택

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **실시간 통신**: Server-Sent Events (SSE)
- **스타일링**: CSS 애니메이션

## 파일 구조

```
vip-rank/
├── app.py              # 메인 애플리케이션
├── requirements.txt    # Python 의존성
├── README.md          # 프로젝트 문서
├── templates/         # HTML 템플릿
│   ├── index.html     # 메인 페이지
│   └── admin.html     # 관리자 페이지
└── static/           # 정적 파일
    ├── word.png      # VIP 로고
    └── pineapple-logo.png  # 파인애플 로고
```

## 배포

### Heroku 배포

1. Heroku CLI 설치
2. Heroku 앱 생성
```bash
heroku create your-app-name
```

3. 배포
```bash
git add .
git commit -m "Initial deployment"
git push heroku main
```

### 다른 플랫폼

- **Railway**: GitHub 연동으로 자동 배포
- **Render**: GitHub 연동으로 자동 배포
- **PythonAnywhere**: 파일 업로드 후 WSGI 설정

## 라이선스

MIT License
