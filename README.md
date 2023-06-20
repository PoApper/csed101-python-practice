# csed101-python-practice

[![Run Tests for Answers](https://github.com/PoApper/csed101-python-practice/actions/workflows/python-tests.yml/badge.svg?branch=main)](https://github.com/PoApper/csed101-python-practice/actions/workflows/python-tests.yml)


## About
포스텍의 프로그래밍과 문제해결 과목 수강생과 파이썬을 처음 배우는 초보자들을 위한 파이썬 연습 문제들을 담은 저장소 입니다.

## Code Problems
포스텍의 `CSED101` 강의 노트 기준으로 연습 문제들이 제공됩니다.

- Memory and Variable
- Input and Output
- Functions and Modules
- Operators and Expressions
- Control Flow
- Data Structure 01 | List, Tuple, Dictionary
- File
- Data Structure 02
- Class and Object-Oriented-Programming

## How to solve problems
0. 기본적으로 컴퓨터에서 파이썬을 실행할 환경을 만들어주세요.  <br />
1. 파일을 다운 받거나 `git`이 설치되어 있을 경우 저장소를 복제해주세요.  <br />
   문제는 파일 별로 독립적으로 존재하므로, 강의 노트마다 존재하는 마크 다운 문서를 읽고 원하는 파일(혹은 문제)을 사용하면 됩니다.  <br />
2. 주석을 잘 읽고, `TODO` 부분에 여러분의 코드를 작성해주세요.  <br />
3. 주어진 코드의 docstring (따옴표 세 개 `"""`로 둘러싸인 설명문)은 테스트에서 사용됩니다. 이 부분은 수정하지 않도록 주의하세요. <br />
4. 작성한 코드의 정확성 검증을 위하여 파일 전체를 실행해 주세요.  <br />
5. 실행한 파일이 `Test passed.`를 출력할 때까지 시도하시길 바랍니다.  <br />

## How to add problem sets
이 단락은 연습 문제를 추가할 때 알아야 할 가장 기본적인 내용에 대해서 다룹니다.  

<br />

- test env

편리한 테스트 코드 작성을 위해, `doctest`를 사용합니다. <a href=https://docs.python.org/ko/3/library/doctest.html>[official doc]</a>  
사용하는 가장 간단한 템플릿은 다음과 같습니다.  
```python
def func():
    """
    >>> func()
    (적당한 실행 결과)
    """
    ...

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```

<br />

- process

문제를 추가하는 1인은 파일 1개를 생성합니다.  
해당 파일에서 일관된 테마의 양질의 문제(함수 구현 등)들을 작성해주세요.  
자신이 해당 문제(혹은 파일)에서 다루는 내용과 가장 흡사한 강의 노트의 폴더에 파일을 추가하여, PR을 올리는 것이 권장됩니다.  

