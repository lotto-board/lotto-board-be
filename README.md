# LOTTO-API
## 버전
### Python Version
```
3.11.6
```

### Run With pyenv
pyenv 설치
```sh
brew install pyenv
brew install pyenv-virtualenv
```

pyenv 설치 버전 확인
```sh
pyenv install --list 
```

pyenv 설치
```sh
pyenv install {VERSION}
```

pyenv 프로젝트 버전 설정
```sh
pyenv virtual env {VERSION} venv
pyenv local {VERSION}
```

## Project Structure
1. config: 설정 및 기타 설정이 필요할 때 사용
2. database: db 관련된 모든 로직 포함
3. model: API Response에 필요한 DTO
4. routes: API routes
5. sql-scripts: initial script for local db (outdated)
6. main.py: 메인


## API-DOC
API TEST
```
http://localhost:8000/docs
```

API READ DOC
```
http://localhost:8000/redoc
```