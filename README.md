# GPT-FSHelper 프로젝트

GPT-FSHelper는 파일 시스템을 기반으로 코딩을 돕는 어시스턴트를 제공하는 프로젝트입니다. 이 프로젝트를 사용하여 코드 작성을 보다 효율적으로 진행할 수 있습니다.

## 설치 방법

1. 이 프로젝트의 저장소를 클론합니다.
   ```
   git clone https://github.com/ai-castle/GPT-FSHelper.git
   ```
2. 프로젝트 디렉토리로 이동합니다.
   ```
   cd GPT-FSHelper
   ```

## 환경 설정

### 가상 환경 생성 및 활성화

Python 가상 환경을 생성하고 활성화합니다.

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 의존성 설치

필요한 Python 패키지를 설치합니다.

```
pip install -r requirements.txt
```

### 환경 변수 설정

`hparams.py.sample` 파일을 `hparams.py`로 복사하고, 필요한 환경 변수를 설정합니다.

```
cp hparams.py.sample hparams.py
```

#### hparams.py 설정

- `OPENAI_API_KEY`: OpenAI API 키를 입력합니다.
- `MODEL_NAME`: 사용할 모델의 이름을 설정합니다.
- `TOKEN_CAL_MODEL_NAME`: 토큰 계산에 사용할 모델의 이름을 설정합니다.
- `PROJECT_ROOT_PATH`: 프로젝트의 루트 경로를 설정합니다.
- `INCLUDED_PATHS`: 포함할 경로 목록을 설정합니다.
- `EXCLUDED_PATHS`: 제외할 경로 패턴을 설정합니다.


## app.ipynb 실행

Jupyter Notebook을 사용하여 `app.ipynb`를 실행합니다. 이 Notebook은 프로젝트의 주요 기능을 제공합니다.

```
jupyter notebook app.ipynb
```

### 사용자 입력

`user_input` 변수에 텍스트를 입력하여 어시스턴트에게 질문하거나 명령을 내릴 수 있습니다.

### 주요 함수와 파라미터

- `get_project_info()`: 프로젝트의 파일 정보를 수집하고, 각 파일의 토큰 수를 계산합니다. 이 함수는 파일 시스템을 탐색하여 프로젝트의 구조를 분석합니다.

- `chat_request(file_contents, prompt_history_queue, user_input, include_file_contents=True, include_prompt_history=True, display_history=False)`: 사용자의 입력을 바탕으로 대화를 진행합니다. 이 함수는 다음 파라미터를 받습니다.
  - `file_contents`: 현재 프로젝트의 파일 내용입니다.
  - `prompt_history_queue`: 이전 대화 내역을 저장하는 데큐입니다.
  - `user_input`: 사용자로부터 받은 입력 텍스트입니다.
  - `include_file_contents`: 대화에 파일 내용을 포함할지 여부를 결정합니다.
  - `include_prompt_history`: 대화에 이전 대화 내역을 포함할지 여부를 결정합니다.
  - `display_history`: 이전 대화 내역을 출력할지 여부를 결정합니다.

## 주의사항

- **환경 변수 설정**: `hparams.py` 파일에 정의된 환경 변수들은 프로젝트의 실행에 필수적입니다. 특히, `OPENAI_API_KEY`는 유효한 OpenAI API 키로 설정되어야 합니다.

- **파일 경로**: `PROJECT_ROOT_PATH`, `INCLUDED_PATHS`, `EXCLUDED_PATHS` 등의 경로 설정은 프로젝트의 구조에 따라 올바르게 조정되어야 합니다.

이러한 단계와 주의사항을 따르면, `app.ipynb`를 통해 프로젝트의 파일 시스템 기반 코딩 어시스턴트 기능을 원활하게 사용할 수 있습니다.