<?php
// 年齢を入力する関数
function input_nenrei() {
    while (true) {
        echo "対象年齢（20～35）以上は？";
        $handle = fopen ("php://stdin","r");
        $in_nenrei = trim(fgets($handle));
        if (!is_numeric($in_nenrei) || intval($in_nenrei) != $in_nenrei) {
            echo "数字（整数）を入れて下さい。\n";
            continue;
        }
        $in_nenrei = intval($in_nenrei);
        if ($in_nenrei < 20 || $in_nenrei > 35) {
            continue;
        } else {
            return $in_nenrei;
        }
    }
}

// データ作成
$data = [
    ['名前' => '田中', '年齢' => 25, '職業' => 'エンジニア'],
    ['名前' => '佐藤', '年齢' => 30, '職業' => 'デザイナー'],
    ['名前' => '鈴木', '年齢' => 28, '職業' => '営業'],
    ['名前' => '山田', '年齢' => 27, '職業' => '人事'],
];

// 年齢が入力年齢以上の人を抽出
$m_nenrei = input_nenrei();
$older_than = array_filter($data, function($row) use ($m_nenrei) {
    return $row['年齢'] >= $m_nenrei;
});

// 結果を表示
if (empty($older_than)) {
    echo "該当データなし\n";
} else {
    foreach ($older_than as $row) {
        echo "名前: {$row['名前']}, 年齢: {$row['年齢']}, 職業: {$row['職業']}\n";
    }
}
?>