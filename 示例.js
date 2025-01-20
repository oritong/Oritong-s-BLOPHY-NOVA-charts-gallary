//模板之Into the zone
/*
4框循环
1节拍切换下一框
事件长度4节拍
*/
CubeEvents.modify('4x cubes', e => {
    e.CenterY(180, 0).ease(Insine).time('4:0/0')
    e.ScaleX(0, 1700).ease(Linear).time('4:0/0')
    e.ScaleY(0, 1700).ease(Linear).time('4:0/0')
    e.Rotate(45, 0).ease(Linear).time('4:0/0')
    e.alpha(0, 255).ease(Linear).time('4:0/0')
})