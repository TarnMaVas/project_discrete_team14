АНАЛІЗ ЗВ’ЯЗНОСТІ ГРАФІВ
Коваль Вікторія, Івасюк Михайло, Бас Юстина, Чеботарьова Юлія,
Тарнавський Максим-Василь

Завдання №1

Читання графу з файлу
Функція: read_csv_non_oriented
Файл читається по рядках, кожен рядок представляє ребро. Для кожного
ребра додаються відповідні вершини у словник як ключі, а значеннями є
список суміжних вершин.
Функція: read_csv_oriented
Аналогічна попередній, але для орієнтованого графу

Завдання №2

Запис графу в файл
Функція: write_file_non_oriented
Створює список ребер для ненапрямленого графа, ітеруючи по
вершинах та їхнім спискам суміжних вершин, та записує цей список у
файл.
Функція: write_file_oriented
Аналогічна попередній, але для орієнтованого графу

Завдання №3

Пошук компонент зв’язності:
Функція: graph_component
Шукає компоненти в неорієнтованому графі, що представлений у
вигляді словника. Кожен ключ вказує на вершину, а значення - це
списки суміжних вершин. Алгоритм використовує метод пошуку в
глибину (DFS). Він формує список з'єднаних компонентів, де кожна
компонента представлена як список вершин.
Примітка:
Правильність введеного графа перевіряється за допомогою функції
'graph_checking'

Завдання №4

Функція tarjans_algorithm використовує алгоритм Тар’яна для
знаходження всіх компонент сильної зв'язності в орієнтованому графі.
Алгоритм працює на основі глибинного пошуку (DFS) та низьких
вказівників: якщо низький вказівник вершини = її індексу, то вона і її
нащадки є компонентою сильної зв'язності. Для реалізації цього в коді
ми використовуємо словники індексів та низьких вказівників indices та
lowlinks відповідно, а також список stack в ролі стеку

Завдання №5

П’ятий пункт реалізовано за допомогою функцій articulation_finder() та
articulation_recursive(), які базуються на алгоритмі Тар’яна. Для початку
пошуку в функцію articulation_finder() передається граф, в ній
ініціюються словник info та список result. Далі вона, за допомогою
articulation_recursive(), проводить модифікований пошук вглиб: при
потраплянні у вершину вона стає ключем info, її значення - список
трьох елементів:
- Порядковий номер вершини (перша вершина - 0, друга - 1…), в
коді порядковий номер відповідає глибині рекурсії;
- Найменший порядковий номер вершини, до якої можна дістатися з
даної вершини, не враховуючи шляху, який привів нас до неї;
- Батько вершини (для кореня (вершини “0”) - None).
Рекурсивно обходячи всі доступні вершини графа, функція паралельно
записує нові вершини в info й змінює другий елемент списків
відповідних вершин, якщо знаходить шлях до меншого порядкового
номера. Таким чином вона перевіряє, чи є кожна вершина єдиним
шляхом, що веде до піддерева її нащадків: якщо її порядковий номер
менший/рівний другому елементу списку її сина, то це правда, а отже
дана вершина - точка сполучення.
Варто зауважити, що для кореня дерева умова буде інша, адже її
порядковий номер завжди задовільняє попередній критерій. Корінь
також буде точкою сполучення, якщо в нього будуть принаймні два
піддерева - нащадки. Для цього в коді використовується лічильник
children.

Завдання №6

Шостий пункт, що полягає в пошуку мостів, використовує функції
bridge_finder() та bridge_recursive() і є дуже подібним на попередній -
він також використовує алгоритм Тар’яна, послідовність дій майже
ідентична. Єдині відмінності - вивід та умови визначення.При
вищезгаданій реалізації ребро між батьком та сином буде мостом лише у
тому випадку, коли порядковий номер батька строго менший за другий
елемент списку сина.
Розподіл роботи

1, 2 функції - Чеботарьова Юлія
3 функція - Івасюк Михайло
4 функція - Коваль Вікторія
5, 6 функції - Тарнавський Максим-Василь
Звіт та презентація - Бас Юстина

Презентація: https://www.canva.com/design/DAF28Kj_FNU/jYipOQC0Y5sX7r7Ro8zuVQ/edit
