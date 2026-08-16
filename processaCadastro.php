<?php

$nome = $_POST["nome"];
$idade = $_POST["idade"];
$profissao = $_POST["profissao"];
$salario = $_POST["salario"];
$experiencia = $_POST["experiencia"];

?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dados do Cadastro</title>

    <link rel="stylesheet" href="style.css">
</head>

<body>

    <div class="container">

        <h1>Dados do Cadastro</h1>

        <p><strong>Nome completo:</strong> <?php echo $nome; ?></p>

        <p><strong>Idade:</strong> <?php echo $idade; ?> anos</p>

        <p><strong>Profissão:</strong> <?php echo $profissao; ?></p>

        <p><strong>Salário pretendido:</strong> R$ <?php echo $salario; ?></p>

        <p><strong>Experiência anterior:</strong> <?php echo $experiencia; ?></p>

        <hr>

        <h2>Mensagem</h2>

        <p>
            Olá, <strong><?php echo $nome; ?></strong>!
            Recebemos seu cadastro para a profissão de
            <strong><?php echo $profissao; ?></strong>.
            Sua experiência informada foi:
            <strong><?php echo $experiencia; ?></strong>.
            Agradecemos seu interesse!
        </p>

        <a href="cadastro.html" class="voltar">
            Voltar ao formulário
        </a>

    </div>

</body>
</html>
