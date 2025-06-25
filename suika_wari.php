<?php

define('BOARD_SIZE', 5);

// x座標とy座標の生成(generate_position)
function generate_position($size) {
    $x = rand(0, $size - 1);
    $y = rand(0, $size - 1);
    return [$x, $y];
}

// ２点間の距離算出(calc_distance)
function calc_distance($pos1, $pos2) {
    $diff_x = $pos1[0] - $pos2[0];
    $diff_y = $pos1[1] - $pos2[1];
    return sqrt($diff_x ** 2 + $diff_y ** 2);
}

// プレイヤーを移動(move_position)
function move_position($direction, $pos) {
    list($current_x, $current_y) = $pos;
    if ($direction === "n") {
        $current_y -= 1;
    } elseif ($direction === "s") {
        $current_y += 1;
    } elseif ($direction === "w") {
        $current_x -= 1;
    } elseif ($direction === "e") {
        $current_x += 1;
    }
    return [$current_x, $current_y];
}

// スイカ割ゲーム(suika_wari)
function suika_wari() {
    $suika_pos = generate_position(BOARD_SIZE);
    $player_pos = generate_position(BOARD_SIZE);

    while ($suika_pos !== $player_pos) {
        $distance = calc_distance($suika_pos, $player_pos);
        echo "スイカへの距離: {$distance}\n";

        echo "n:北に移動 s:南に移動 e:東に移動 w:西に移動 > ";
        $c = trim(fgets(STDIN));
        $player_pos = move_position($c, $player_pos);
    }

    echo "スイカを割りました！\n";
}

// スイカ割ゲームStart
suika_wari();

?>