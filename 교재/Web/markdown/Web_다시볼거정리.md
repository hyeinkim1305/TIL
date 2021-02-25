# 다시 볼거 정리

*W3C / WHATWG*

*HTML : hyper text markup language*

*HTTP : hyper text transfer protocol*

*html요소는 태그와 내용으로 구성*

- *시맨틱태그*

*header : 문서 전체나 섹션의 헤더*

*nav : 내비게이션*

*aside : 사이드에 위치한 공간, 메인 컨텐츠와 관련성이 적은 콘텐츠*

*section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현*

*article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역*

*footer : 문서 전체나 섹션의 푸터* 

- *그룹컨텐츠*

*p / hr / ol / ul / pre / blockquote / div*

- *텍스트 관련 요소*

*a / b , strong / i, em / span , br , img*

- *form : 서버에서 처리될 데이터를 제공하는 역할*

*action / method*

- *label : 서식 입력 요소의 캡션*
- *input : 공통 속성 (name / placeholder / required / autofocus)*

*CSS : cascading style sheets*

*css 정의방법 : 인라인, 내부참조, 외부참조*

*HTML 문서에서 특정한 요소를 선택해 스타일링 하기 위해서는 반드시 선택자라는 개념이 필요*

- *css 우선순위*

*!important / 인라인 / id선택자/ class 선택자 / 속성 선택자 / 요소 선택자 / 소스순서*

*상속되는 것 ; Text 관련 요소*

*상속 안되는 것 : Box model. position*

- *크기 단위*

*em : 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐*

*rem : 최상위 요소의 사이즈를 기준으로 배수 단위를 가짐*

*margin은 배경색을 지정할 수 없다.*

*padding > 요소에 적용된 배경색, 이미지는 padding까지 적용됨*

- *margin*

*margin 10px 20px : 상하 / 좌우*

*margin 10px 20px 30px : 상 좌우 하*

*margin 10px 20px 30px 40px : 시계방향*

*상하 margin은 상쇄 일어남*

- *box-sizing : border-box*

- *블록레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음* 
- *인라인 요소 : content 너비 만큼 가로 폭을 차지 / width, height, margin-top, margin-bottom 을 지정할 수 없다. / 상하 여백은 line-height로 지정*
- *대표적인 블록레벨 요소 : div / ul, ol, li / p / hr/  form*
- *inline-block : inline 처럼 한 줄에 표시 가능하며, block 처럼 width, height, margin 속성을 모두 지정할 수 있다.*
- *display none / visibility : hidden (해당 요소가 공간은 차지 / 화면에 표시만 하지 않는다 )*
- *relative : static 위치를 기준으로 이동*
- *float clear  :  부모요소에 적용*

```html
.clearfix::after {
content:"";
display: block;
clear: both;
}
```

- *flex*

*flex container안에 flex item*

*부모요소에 display: flex 라고 시작*

- *bootstrap*

*부트스트랩 그리드 시스템은 flexbox로 제작됨*

*container, rows, column으로 컨텐츠를 배치하고 정렬*

*12개의 column, 6개의 grid breakpoints*

- 



