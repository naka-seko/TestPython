<?php
// リストオブジェクト anc --> ABC
$list_obj = ["apple", "orange", "banana"];
foreach ($list_obj as $fruit_name) {
    $upper_name = strtoupper($fruit_name);
    echo $upper_name . PHP_EOL;
}

// タプルオブジェクト anc --> ABC
// PHPにはタプルはありませんが、配列で代用します
$tuple_obj = ["apple", "orange", "banana"];
foreach ($tuple_obj as $fruit_name) {
    $upper_name = strtoupper($fruit_name);
    echo $upper_name . PHP_EOL;
}

// 文字列オブジェクト hello --> HELLO
$str_obj = "hello";
for ($i = 0; $i < strlen($str_obj); $i++) {
    $upper_letter = strtoupper($str_obj[$i]);
    echo $upper_letter . PHP_EOL;
}

// 辞書オブジェクト English --> Japanese
$dict_obj = ["dog" => "犬", "cat" => "猫", "parrot" => "オウム"];
foreach ($dict_obj as $english => $japanese) {
    echo $english . " は " . $japanese . " です。" . PHP_EOL;
}
?>