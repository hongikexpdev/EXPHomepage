# 소개

* [강의](https://speakerdeck.com/rijgndqw012/python-web-development)

* 이 프로젝트는 홍익대학교 게임동아리 EXP의 게임개발 스터디 참고자료로 만든 프로젝트입니다.
 * 게임개발과 직접적인 연관은 없지만, Tool engineering의 개념을 소개하면서 Flask 사용을 고려하게 됬습니다.

* 홍익대학교 컴퓨터공학과 알고리즘 소모임 HI-ARC에서 Flask 사용법을 교육하기 위해 참고하는 프로젝트이기도 합니다. 
* 재활용을 고려해서, 앞으로도 추가되었으면 내용들을 이슈로 등록해주시면 되겠습니다.

## 사용법

* 준비물 : python, pip

 1) windows <br>
  * [python 공식 홈페이지](https://python.org)에서 최신버전으로 다운로드(3.5)
   * (옵션) `제어판 > 시스템 및 보안 > 시스템`에서 `고급 시스템 설정 > 고급 탭 > 환경 변수 (Advanced system setting > Advanced > Environment variables)`로 들어간다. 시스템 변수에서 Path 변수를 클릭하여 수정. Path 변수의 값 맨 오른쪽에 `;` 를 붙이고 python이 설치된 경로를 입력. (예시: Path -> `C:\Program Files\Blah;C\Python35`) 여기서 `;` 는 경로 간의 구분자 역할을 해준다.   
  * [여기서](https://bootstrap.pypa.io) get-pip.py 파일을 내려받고, python get-pip.py 로 pip를 설치한다. <br>

 2) mac : brew install python
  * (옵션)
  ```sh
  brew install pyenv
  pyenv install 3.5.0
  pyenv global 3.5.0
  ```
 3) linux : sudo apt-get install python
  * (옵션)
  ```sh
  git clone https://github.com/yyuu/pyenv.git ~/.pyenv
  
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

  echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
  ```
   * `~/.bash_profile` 관련 : Ubuntu일 경우 `~/.bashrc`로 수정. zsh를 기본 셸로 사용하는 경우, `~/.zshrc`로 수정한다.
  * (옵션2) [python-build](https://github.com/yyuu/pyenv/tree/master/plugins/python-build)를 이용한 설치
  
```sh
$ git clone https://github.com/malkoG/flask-demo
$ cd flask-demo
$ python app.py
```

**PROFIT!**

## Flask로 시작하는 웹프로그래밍 튜토리얼

Flask로 웹프로그래밍을 시작하기 위해 먼저 알아둬야하는 몇가지 배경지식이 있는데, 다음의 링크를 참고해둘 필요가 있다.

* [Python](https://python.org) : 메인으로 쓰는 프로그래밍 언어
 * [Codecademy](https://www.codecademy.com/learn/python) : interactive한 강의 구성으로 빠르게 배우기 쉬움. python 튜토리얼 중에서 최고봉
* [HTML](http://www.w3schools.com/html/default.asp) : 웹페이지를 생성할 때 사용하는 마크업 언어
 * [Codecademy](https://www.codecademy.com/learn/web)
* [CSS](http://www.w3schools.com/css/default.asp) : HTML로 생성한 페이지를 다채롭게 꾸밀때 사용
* [Javascript](http://www.w3schools.com/js/default.asp)
 * [Codecademy](https://www.codecademy.com/learn/javascript)


## 구조(라 할 것도 없다)

```
.
├── README.md
├── app.py
├── static
│   ├── style.css
│   └── style1.css
└── templates
    ├── a.html
    ├── b.html
    ├── c.html
    ├── layout-bootstrap.html
    └── layout.html
```

## Flask로 개발하면서 참고해볼만한 공식문서

* **Python**
 * [파이썬 표준 라이브러리](https://docs.python.org/3.5/library/) : 파이썬에서 디폴트로 지원하는 여러가지 함수들을 설명
 * [Flask](http://flask.pocoo.org) : 플라스크 사용법을 알려줌
   * [한글판](http://flask-docs-kr.readthedocs.io/ko/latest/)
   * [Jinja](http://jinja.pocoo.org) : 템플릿 엔진
 * [SQLAlchemy](http://www.sqlalchemy.org) : ORM(객체-관계 매퍼), 데이터베이스 이용 시 참고.
 * [scrapy](http://scrapy.org) : 웹 스크래핑
 * [pandas](http://pandas.pydata.org/index.html) : csv, xlsx, json 파일을 긁어서 행렬의 형태로 변환. 데이터 분석용으로 이용 
 * [matplotlib](http://matplotlib.org) : 플롯 차트를 그려주는 유용한 라이브러리
* **HTML/CSS/Javascript** : 웹표준문서를 링크하지 않겠지만, 세련된 UI로 빠르게 개발하는데 도움이 되는 라이브러리를 소개한다.
 * [Bootstrap](http://getbootstrap.com) : Twitter 개발.
 * [Pure](http://purecss.io) : Yahoo 개발.
 * [Foundation](http://foundation.zurb.com)
* **Web Frontend Framework** : 좀 더 복잡한 UI/UX를 추가하고자 할 때 도움이 되는 라이브러리를 소개한다.
 * [Backbone.js](http://backbonejs.org)
 * [Angular.js](https://angularjs.org) : Google 개발. MVC 패턴을 따르는 프론트엔드 프레임워크
 * [React.js](https://facebook.github.io/react/) : Facebook 개발. 기존의 MVC 패턴에 반하는 새로운 개념의 패턴을 제시

## Best Practice

