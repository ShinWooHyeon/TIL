# Positing for Css Layout
- CSS Position이란 Normal Flow 요소를 다른 위치로 배치하는 것이다.
- 이동 방향은 X,Y, Z(`Z-index`) 세 방향이다.
- Position 유형은 Static(기본),Relative(상대),Absolute(절대),Fixed(고정),Sticky(상황에 맞춰 변하는 특징)
## Positioning Type
- Position
    - Static (기본값,Normal Flow)
        - 본인 위치의 너비를 차지
    - Relative(Normal Flow)
        - 자기 자신을 기준으로 이동한다
        - 요소가 차지 하는 공간은 static일 때와 동일하다

    - Absolute (요소를 Normal Flow에서 제거 )
        - 본인의 영역만 너비를 차지
        - 본인 위치가 없어지고 자신이 나간 위치에 아래 요소들이 올라온다(`아래에만 적용,위에는 적용x`) 
        - 가장 가까운 부모(`Relative`)요소를 기준으로 이동한다
    - Fixed (요소를 Normal Flow에서 제거)
        - 현재 화면영역(viewport) 기준으로 이동
        - 본인 위치가 없어지고 자신이 나간 위치에 아래 요소들이 올라온다
    - Sticky(Normal Flow)
        - 가장 가까운 block 부모 요소를 기준으로 이동한다
        - 요소가 특정 `임계점`에 스크롤 될 때 고정된다(`fixed`)
        - 다음 sticky 요소가 나오면 그 sticky요소가 이전 sticky 요소 자리를 대체한다.(`위치가 겹쳐지기 때문`)
- 요소들 이동하는데 사용하는 코드
    - Transform: 요소를 x,y 기준으로 이동시킨다 (오른쪽 아래가 x(+),y(+))
    - line-height:텍스트 라인의 높이 , 컨텐츠의 길이만큼 주면 가운데로 가게 된다.
    - ex. 중앙으로 absolute 이동 => left top 50%로 중앙위치(기준점이 중앙 ), 기준점을 중앙으로 바꾸기 위해 transform : translate(-50%,-50%)하면 중앙배치가능

## Z-index
- 요소가 겹쳤을 때 요소들이 화면에 보이는 우선순위
- 정수 값을 사용해 z축 순서를 결정하며 큰 값의 요소가 작은 값의 요소를 덮는다
- 기본값은 `0`