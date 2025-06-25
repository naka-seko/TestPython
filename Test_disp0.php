<?php
// 年齢を入れる
function input_nenrei() {
    while (true) {
        echo "年齢はいくつですか？(0～120) ";
        $in_age = trim(fgets(STDIN));
        if (!is_numeric($in_age) || intval($in_age) != $in_age) {
            echo "数字（整数）を入れて下さい。\n";
            continue;
        }
        $in_age = intval($in_age);
        if ($in_age < 0 || $in_age > 120) {
            continue;
        } else {
            return $in_age;
        }
    }
}

// 身長を入れる
function input_height() {
    while (true) {
        echo "身長は何センチ？(100～300) ";
        $in_height = trim(fgets(STDIN));
        if (!is_numeric($in_height)) {
            echo "数字（小数点１桁迄）を入れて下さい。\n";
            continue;
        }
        $in_height = floatval($in_height);
        if ($in_height < 100 || $in_height > 300) {
            continue;
        } else {
            return $in_height;
        }
    }
}

// 年齢と身長の初期値
$min_age = 10;
$min_height = 110.0;

// 年齢と身長を入れる
$age = input_nenrei();
$height = input_height();

// 判定処理
if ($min_age <= $age && $min_height <= $height) {
    echo "お乗りいただけます\n";
} else {
    echo "ご遠慮ください\n";
}
?>