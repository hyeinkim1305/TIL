# Git

### 초기설정

- git 추가할때

  ```
  git init
  touch .gitignore   #ignore파일만든다
  touch .README.md
  
  ```

- clone받을때

  ```
  git clone 혹은
  git init 
  git remote add origin url
  git remote -v
  ```

### 파일 올리기

```
git status
git add
git commit -m ""
git push
```

### 파일받아오기

```
git pull origin master
```

-----------

### 그 외 사항

- add를 취소할 때

  ```
  gir rm --cached 파일이름
  ```

  이런거할 때 git status 찍어보고 거기서 알려주는거로 사용하는게 좋음

- 방금 내가 남긴 커밋을 취소할 때

  ```
  git commit --amend
  ```

  i는  끼워넣기 모드, esc는 취소모드
  
  오타를 쭉 지워준다. 그리고 esc눌러서 취소해줌.
  
  :을 입력하고 wq를 넣어준다. (저장하고 나가겠다)
  
- 빠뜨리고 commit했을 때 인듯

  ```
  git commit --amend
  ```

- 이전 커밋 내용으로 돌아갈때

  1) hard

  ```
  git log --oneline   # 커밋들보기
  git reset --hard 커밋이름
  ```

  코드까지 그 상태로 돌아감

  2) soft

  ```
  git log --oneline   # 커밋들보기
  git reset --soft 커밋이름
  ```

  커밋은 그때로 돌아갔는데 코드는 그대로임
