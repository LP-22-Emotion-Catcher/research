<h2>Гайд по работе с API VK и извлечению информации со стен групп:</h2>

1) Следуем процедуре, описанной здесь: https://vk.com/dev/first_guide"<br>
    а) Создаем Standalone-приложение <br>
    б) Получаем токены и ключи

2) Клониируем наш репозиторий, добавляем в файл config.py строки: <br>
    а) <b>access_token</b> = "Ваш токен" <br>
    б) <b>owner_id</b> = "ID группы или человека в VK"

3) Устанавливаем все пакеты и библиотеки через <b>poetry</b>

4) Запускаем <b>jupyter notebook</b> и в нем открываем new_vk_wall_handler.ipynb

5) Активируем блоки с кодом и визуализируем результат, а именно:

На выходе имеем Csv файл, который можно как просмотреть в Excel, так и визуализировать с помощью библиотеки Pandas (что продемонстрировано), содержащий таблицу с ячейками:
    
 - дата публикации сообщения<br>
 - кол-во лайков<br>
 - кол-во репостов<br>
 - кол-во просмотров<br>
 - кол-во комментариев<br>
 - текст публикации<br>
 - содержание вложения к публикации<br>
 - ссылка на публикацию<br>
  