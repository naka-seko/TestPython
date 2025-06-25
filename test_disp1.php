<?php
// 人数を入れる(0～9999)
function input_kensu() {
    while (true) {
        $in_kensu = readline("(End:9999) ");
        if (!is_numeric($in_kensu) || strpos($in_kensu, ".") !== false) {
            echo "数字（整数）を入れて下さい。\n";
            continue;
        }
        $in_kensu = (int)$in_kensu;
        if ($in_kensu < 0 || $in_kensu > 9999) {
            continue;
        } else {
            return $in_kensu;
        }
    }
}

// 合計値, 平均値, 件数の算出
function total_and_average_and_number($values) {
    $total = array_sum($values);
    $num = count($values);
    $average = $num > 0 ? $total / $num : 0;
    return [$total, $average, $num];
}

// メインルーチン
$values = [];
$index = 0;
$max_index = 6; // 日付数は1週間(7日)

while ($index <= $max_index) {
    echo ($index + 1) . "日目は何件ですか？\n";
    $in_kensu = input_kensu();

    if ($in_kensu == 9999) {
        if ($index == 0) {
            $values = [0];
        }
        break;
    }

    $values[$index] = $in_kensu;
    $index++;
}

list($total, $average, $number) = total_and_average_and_number($values);
echo "[" . implode(", ", $values) . "] の 合計は $total 平均は $average 件数は $number です。\n";
?>