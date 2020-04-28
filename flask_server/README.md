* 현재 패스트 스타일 트랜스퍼에서 사용가능한 모델 이름

creation_of_adam_models,
Mondrian_models
the_starry_night_models
white_cow_models

* 주의사항

모델은 FastStyleTransfer 하위에 압축을 풀어서 넣는다

* post요청 보낼 때 방식

폼 데이터에 ex)creation_of_adam_models와 같이 모델명을 텍스트 형식으로 폼데이터에 append해서 'type'로 보내고, 파일은 'photo'로 보낸다(탭에서 선택하면 자동으로 text가 선택되게 하면 될듯)

(어떻게 보내는지 알기 어려울 시 첨부된 web/component의 axios 부분을 참고한다.)

