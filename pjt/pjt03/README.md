# PJT 03



#### > 개발 목표

##### 반응형 웹 페이지 구성

> HTML을 통한 웹 페이지 마크업 분석
>
> CSS 라이브러리의 이해와 활용
>
> 컴포넌트 및 그리드 시스템 활용
>
> 커뮤니티 서비스 반응형 레이아웃 구성



#### > 개발 도구

> Visual Studio Code
>
> Google Chrome Browser
>
> Bootstrap v5.0



#### >  완성한 웹 페이지

- 전체화면 (Home, Community, Login)

![ezgif.com-gif-maker (1)](README.assets/ezgif.com-gif-maker (1).gif)



- 작은 화면 (Home)

![ezgif.com-gif-maker (2)](README.assets/ezgif.com-gif-maker (2).gif)



- 작은 화면 (Community)

![ezgif.com-gif-maker (3)](README.assets/ezgif.com-gif-maker (3).gif)





### 01_nav_footer

- 네비게이션 상단바 햄버거 버튼 교체

  ```html
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
  ```

  ```html
  <div class="collapse" id="navbarToggleExternalContent">
      <div class="bg-dark p-2">
        <li class="pt-2"><a class="link-light text-decoration-none" href="02_home.html">Home</a></li>
        <li class="pt-2"><a class="link-light text-decoration-none" href="03_community.html">Community</a></li>
        <li class="pt-2"><a class="link-light text-decoration-none" href="#">Login</a></li>
      </div>
    </div>
  ```

  > 새로 알게 된 점

  Bootstrap의 Nav 부분을 활용하면 기존 네비게이션 바 모양에서 화면 픽셀크기가 줄어들었을 때 목록 형식으로 바뀌는 것을 만들 수 있다. 또한 아래에 있는 코드는 Nav에서 위로 글이 올라오는 것 예제를 변형하여 아래로 글 형식이 가게 만들었다. 

  > 아쉬운 점

  크롬 브라우저로 확인하니 목록 아이콘을 눌렀을 때 픽셀크기가 클 때 있던 네비게이션 리스트들이 나타났다. 햄버거 버튼의 세부 항목을 만드는 것에 집중을 하다 뒤늦게 알게 되어 아쉬웠다. 오늘 안에 수정해보리라....

  > 뒤늦게 수정한 점 🤣🤣🤣

  ❗❗ Bootstrap의 Navbar 화면을 픽셀을 줄여서 보니 기본 Navbar 햄버거 버튼에 리스트 형식이 내장되어 있는 것이었다 !!!!! 내장되어 있는지 모르고 햄버거 버튼의 세부 항목을 새로 만들어보고 뭔가 고치는 과정에서 실수가 있었던 것 같다... 진짜 바보같았다 Docs를 잘 살펴보자는 교훈을 얻었다.. 

  TIL에 올릴 프로젝트에는 네비게이션바를 고쳐보았다.

  ![ezgif.com-gif-maker (4)](README.assets/ezgif.com-gif-maker (4).gif)

  

- 로그인 리스트 클릭 시 양식 등장

  > 새로 알게 된 점

  modal이 처음에는 뜨기만 하고 회색 창이 유지되어 고민했다. Nav태그 밖으로 꺼내면 제대로 작동된다는 것을 알게 되었다. Modal과 Form을 같이 사용해 완성할 수 있었다. 



### 02_home

- 화면 사진 슬라이드

  > 새로 알게 된 점

  Bootstrap의 carousel 기능을 가져와 사용해보는 것을 연습할 수 있었다. 

- 영화 사진들 픽셀 크기별 배치

  ```html
  <section class="container">
      <div class="row row-cols-1 row-cols-sm-2 g-4">
        <article>
          <div class="col">
            <div class="card">
              <img src="images/movie1.jpg" class="card-img-top" alt="...">
              <div class="fw-bold card-body d-flex flex-column align-items-center">
                <a href="#" class="text-dark text-decoration-none">Movie Title</a>
                <p class="card-text">This is a longer card with supporting text below as,,,</p>
              </div>
            </div>
          </div>
  ```

  > 새로 알게 된 점

  부트스트랩의 Grid 기능을 사용하기 위해 section에 클래스를 주고 article들을 묶어 row와 row-cols-1 이런 식으로 픽셀 별 나타나는 열 수를 정해주었다. 여러 article들에 배열을 주는 것을 다시 연습해볼 수 있었다. 



### 03_Community

- 게시판 목록과 table 배치

  ```html
  <div class="main container">
      <div><h1 class="text-center m-5">Community</h1></div>
      
      <div class="row">
        <aside class="col-12 col-lg-2">
          
          <ul class="list-group">
            <li class="list-group-item"><a href="#" class="text-decoration-none">Boxoffice</a></li>
            <li class="list-group-item"><a href="#" class="text-decoration-none">Movies</a></li>
            <li class="list-group-item"><a href="#" class="text-decoration-none">Genres</a></li>
            <li class="list-group-item"><a href="#" class="text-decoration-none">Actors</a></li>
          </ul>
          
        </aside>
  ```

  > 새로 알게 된 점

  container와 row, col 등을 활용하는 것이 예제가 아닌 홈페이지에 실제로 적용하려니 헷갈렸다. 각 태그들을 어떻게 묶었는지에 따라 배치가 매우 달라질 수 있음을 알게 되었다. 

  가장 밖은 ( container >  community 글자, row, 글목록 ) 으로 묶었고, row에는 ( row > 리스트 목록, 표, pagination )으로 해서 묶은 뒤 각 리스트 목록과 표는 col을 이용해 배치하고, d-none, d-lg-table을 이용해 픽셀 크기 당 나타나는 부분을 정해주었다. pagination 또한 비슷한 방법으로 처리한 뒤 d-flex를 이용해 중앙정렬 해주었다. 

  display에 있는 d-none과 d-lg-block과 같은 것들은 새롭게 알게 되었다. 유용한 기능인것같다..!!!

  > 아쉬운 점

  처음에 게시판 목록과 표를 배치할 때 머리속이 복잡해졌다.. 오늘 배운 내용들을 잘 복습해서 익혀두자!!

