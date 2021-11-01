## Лабораторная работа "Файловый менеджер" по Практикуму по программированию 
### Цель лабораторной работы
Научиться создавать сложный проект и научиться программно работать с локальными файлами и папками.
### Задания для выполнения
Необходимо создать примитивный файловый менеджер. Программа должна работать в определенной папке (рабочей папки менеджера) и позволять пользователю выполнять следующие простые действия в пределах рабочей папки:
1. Создание папки (с указанием имени);

![image](https://user-images.githubusercontent.com/70855182/139688510-2b5582f2-cc9d-4426-a977-4595a692d472.png)

![image](https://user-images.githubusercontent.com/70855182/139688612-b1dffee3-0248-4ac4-b69f-2055fe7b76f1.png)

![image](https://user-images.githubusercontent.com/70855182/139688693-1c6b9a2a-492e-485a-9dfb-ae06043e6b46.png)

2. Удаление папки по имени;

![image](https://user-images.githubusercontent.com/70855182/139688837-5774863b-e0e6-4281-ad18-c369ece7b7ae.png)

![image](https://user-images.githubusercontent.com/70855182/139688897-b4f4ecf2-7649-485a-989e-5970753cbf32.png)

Если попытаться удалить несуществующую папку:

![image](https://user-images.githubusercontent.com/70855182/139688999-c598329b-620f-403d-a0d5-e5ca0ad0b7fd.png)

3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;

![image](https://user-images.githubusercontent.com/70855182/139689145-e597edc5-ed35-4c05-9c33-d2a4eefa9358.png)

![image](https://user-images.githubusercontent.com/70855182/139689197-5cd5ca7e-075a-4daf-bc6b-71947d9d6f1b.png)

![image](https://user-images.githubusercontent.com/70855182/139689229-aac435c5-d19e-4b02-9a0d-fb2898aad07c.png)

![image](https://user-images.githubusercontent.com/70855182/139689261-2bdbea02-495f-4275-92f5-0daf3b9a472d.png)

Если попытаться перейти в несуществующую папку:

![image](https://user-images.githubusercontent.com/70855182/139689347-b70b6ec2-de2e-47e8-8bca-4549a2d296cc.png)

4. Создание пустых файлов с указанием имени;

![image](https://user-images.githubusercontent.com/70855182/139689512-13ead54d-2ac7-4173-97fc-b68fb0221b2a.png)

![image](https://user-images.githubusercontent.com/70855182/139689557-c7cffcc4-50eb-47a7-9b7c-bca17de4a366.png)

5. Запись текста в файл;

![image](https://user-images.githubusercontent.com/70855182/139689983-9d4c70c5-5f85-4d2e-9564-c467391f4cb7.png)

![image](https://user-images.githubusercontent.com/70855182/139690033-b8643bdc-b30c-4e77-8a6c-a443d4914fba.png)

Если попытаться редактировать несуществующий файл:

![image](https://user-images.githubusercontent.com/70855182/139690141-8560da8d-fdf3-4683-b009-7bad41addd2c.png)

6. Просмотр содержимого текстового файла;

![image](https://user-images.githubusercontent.com/70855182/139690408-1c02a202-0111-45e4-bb8d-f89469040934.png)

![image](https://user-images.githubusercontent.com/70855182/139690328-39f82625-45f1-418e-824b-11cee3f7f223.png)

7. Удаление файлов по имени;

![image](https://user-images.githubusercontent.com/70855182/139690666-d103654b-e939-4cf9-bc57-a04298583f0e.png)

![image](https://user-images.githubusercontent.com/70855182/139690702-82ea31e9-ccd0-4d0a-bb2d-94bd016a2ec5.png)

8. Копирование файлов из одной папки в другую;

![image](https://user-images.githubusercontent.com/70855182/139692489-de9e9ea1-795a-4889-83a4-1c9955449de0.png)

![image](https://user-images.githubusercontent.com/70855182/139692549-4b48de4c-cea9-437a-a73d-b91979f17320.png)

9. Перемещение файлов;

![image](https://user-images.githubusercontent.com/70855182/139692719-7dd187f2-e3cd-4c01-9816-26c45e21875f.png)

![image](https://user-images.githubusercontent.com/70855182/139692905-dbc6cff8-92f0-4272-be87-72ac9c8173b0.png)

![image](https://user-images.githubusercontent.com/70855182/139692973-d79de41b-860f-439d-92ff-b400718d2b86.png)

10. Переименование файлов.

![image](https://user-images.githubusercontent.com/70855182/139692175-9dd51b73-0700-427a-9034-06368edb87cb.png)

![image](https://user-images.githubusercontent.com/70855182/139692204-5aea789e-de8f-48ba-9e88-37dc8b9595cd.png)

Дополнительные задания

1. Разработайте псевдографический интерфейс для разработанного в основном задании файлового менеджера.

![image](https://user-images.githubusercontent.com/70855182/139693419-18b29a44-9567-4490-8aaf-330864dc4b6b.png)

2. Сделайте файловый менеджер многопользовательским. Добавьте возможность регистрации пользователей. При регистрации каждому пользователю создается своя домашняя папка, в пределах которой он может работать.

![image](https://user-images.githubusercontent.com/70855182/139693367-a9264d79-ebab-4cdc-a00f-767a4a2898b0.png)

3. Придумайте и добавьте дополнительные функциональные возможности для файлового менеджера. Как пример можно взять:

Архивация и разархивация файлов и папок;

![image](https://user-images.githubusercontent.com/70855182/139693084-075468ae-fdd2-4ed5-823b-db753586d20c.png)

![image](https://user-images.githubusercontent.com/70855182/139693126-7077e286-2bee-4ed9-81ac-93ea668adc7e.png)

![image](https://user-images.githubusercontent.com/70855182/139693167-84ad235e-b707-4e2c-9ce2-1f9c16e15880.png)

![image](https://user-images.githubusercontent.com/70855182/139693231-567e00f7-c6b8-4c72-be93-5ca1f4c3ec26.png)

