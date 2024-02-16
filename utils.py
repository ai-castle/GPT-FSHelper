import tiktoken
import fnmatch
import os
import hparams as hp
import numpy as np

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
  """Returns the number of tokens used by a list of messages."""
  try:
      encoding = tiktoken.encoding_for_model(model)
  except KeyError:
      encoding = tiktoken.get_encoding("cl100k_base")

  if model == "gpt-3.5-turbo-0613":  # note: future models may deviate from this
    try : 
      num_tokens = 0
      for message in messages:
          num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
          for key, value in message.items():
              num_tokens += len(encoding.encode(value))
              if key == "name":  # if there's a name, the role is omitted
                  num_tokens += -1  # role is always required and always 1 token
      num_tokens += 2  # every reply is primed with <im_start>assistant
      return num_tokens
    except :
        return np.nan
  else:
      raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
  See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")
      
      
      

def is_excluded(path, base, excluded_paths):
    """Check if the path matches any of the exclusion patterns."""
    rel_path = os.path.relpath(path, base).replace(os.sep, '/')
    for pattern in excluded_paths:
        normalized_pattern = pattern.strip('/').replace('/', os.sep)
        if fnmatch.fnmatchcase(rel_path, normalized_pattern) or fnmatch.fnmatchcase(path, normalized_pattern):
            return True
    return False

def list_files(root_path, included_paths, excluded_paths):
    file_list = []

    for included_path in included_paths:
        full_path = os.path.normpath(os.path.join(root_path, included_path.strip("/")))
        for root, dirs, files in os.walk(full_path, topdown=True):
            # Check and remove excluded directories before descending into them
            dirs[:] = [d for d in dirs if not is_excluded(os.path.join(root, d), root_path, excluded_paths)]

            for file in files:
                file_path = os.path.join(root, file)
                if not is_excluded(file_path, root_path, excluded_paths):
                    file_list.append(file_path)
    
    file_list.sort()
    return file_list


def generate_file_content_string(project_root_path, file_path):
    file_content_str = ""  # 결과 문자열 초기화
    # 프로젝트 루트 경로를 제거하여 상대 경로 생성
    relative_path = os.path.relpath(file_path, project_root_path)
    file_content_str += f"[path] /{relative_path}\n"
    try:
        # 파일을 텍스트 모드로 열기 시도
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()  # 파일 내용 읽기
            # 상대 파일 경로와 내용을 포맷에 맞게 추가
            file_content_str += f"[content]\n{content}\n\n"
    except UnicodeDecodeError:
        # 텍스트 파일이 아닌 경우
        file_content_str += "\n"
    except Exception as e:
        # 기타 예외 처리
        file_content_str += f"[content] Error reading file: {str(e)}\n\n"

    return relative_path, file_content_str


