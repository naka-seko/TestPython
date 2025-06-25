<?php
// ループ(while) Test Source
$text = "";
$end_text = "finish";

while ($text !== $end_text) {
    // 文字を入力する
    echo $end_text . PHP_EOL;
    $text = readline("と入力してください:");

    echo $text . " と入力されました。" . PHP_EOL;
}

echo "終了しました。" . PHP_EOL;

// 辞書オブジェクト Test Source
function disp_english_words($english_words) {
    echo count($english_words) . PHP_EOL;

    foreach ($english_words as $english => $dic_word) {
        echo $english . " : " . $dic_word . PHP_EOL;
    }
}

// 辞書オブジェクトメイン
$english_words = [
    "apple" => "りんご",
    "orange" => "みかん",
    "peach" => "もも"
];
disp_english_words($english_words);

// 辞書を追加
$english_words["banana"] = "バナナ";
disp_english_words($english_words);

// 辞書を置換
$english_words["banana"] = "スイートバナナ";
disp_english_words($english_words);

// 辞書を削除
unset($english_words["orange"]);
disp_english_words($english_words);

// 該当辞書を出力
$key = readline("英単語を入力してください：");

if (array_key_exists($key, $english_words)) {
    echo "日本語：" . $english_words[$key] . PHP_EOL;
} else {
    echo "その英単語に対する辞書は有りません。" . PHP_EOL;
}
?>