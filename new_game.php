<?php
session_start();

// ランダムな正解の数字をセッションに保存
if (!isset($_SESSION['answer'])) {
    $_SESSION['answer'] = rand(1, 100);
    $_SESSION['tries'] = 0;
}

$message = "";

if (isset($_POST['guess'])) {
    $guess = intval($_POST['guess']);
    $_SESSION['tries']++;

    if ($guess > $_SESSION['answer']) {
        $message = "もっと小さい数字です。";
    } elseif ($guess < $_SESSION['answer']) {
        $message = "もっと大きい数字です。";
    } else {
        $message = "正解です！{$_SESSION['tries']}回目で当たりました。";
        // ゲーム終了、再スタート用にセッション削除
        session_destroy();
    }
}
?>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>数当てゲーム</title>
</head>
<body>
    <h1>数当てゲーム</h1>
    <p>1から100までの数字を当ててください。</p>
    <?php if (!empty($message)) echo "<p>{$message}</p>"; ?>
    <?php if (!isset($_POST['guess']) || ($_POST['guess'] != $_SESSION['answer'])): ?>
    <form method="post">
        <input type="number" name="guess" min="1" max="100" required>
        <button type="submit">予想する</button>
    </form>
    <?php else: ?>
    <form method="post">
        <button type="submit">もう一度遊ぶ</button>
    </form>
    <?php endif; ?>
</body>
</html>