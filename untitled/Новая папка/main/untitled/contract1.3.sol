pragma solidity ^0.5.0;
contract Store {

    struct User {
        address user_address;
        string name;
        uint category;
            //1 - прочая тайна
            //2 - коммерческая тайна
            //3 - общедоступно
        uint role;
            //0 - бан
            //1 - адмиг
            //2 - библиотекарь
            //3 - обычный пользователь
        string open_key;
    }
    
    struct File {
        uint file_id;
        string title;
        string  author;
        uint tipe;
        uint category;
        uint period;
        string  file_hash;
        uint[] viewtime;
        address[] viewers;
        bool[] viewstatus;
        bool confirmed;
    }
    
    struct Request {
        address user_address;
        uint new_role;
        uint new_category;
    }
    
    Request[] requests;
    File[] files;
    User[] users;
    
    uint Etherium_speed = 14;
    
    constructor() public {
        users.push(User(0x0000000000000000000000000000000000000000, "0", 0, 0, "000"));
    }
    
    modifier isAdmin {
        uint user_id = get_user_id_by_user_address(msg.sender);
        require(users[user_id].role == 1, "not admin");
        _;
    }  
    
    modifier isLibr {
        uint user_id = get_user_id_by_user_address(msg.sender);
        require(users[user_id].role == 2, "not librarian");
        _;
    }
    
    //Создать 2 админа, 2 библиотекаря
    function admin_genesis(address admin_address, string memory name, string memory open_key) public {
        users.push(User(admin_address, name, 3, 1, open_key));
    }
    
    function libr_genesis(address libr_address, string memory name, string memory open_key) public {
        users.push(User(libr_address, name, 0, 2, open_key));
    }
    
    //Получить номер пользователя по адресу - Работает
    function get_user_id_by_user_address(address user_address) public view returns(uint user_id) {
        for (uint i=0; i<users.length; i++) {
            if (users[i].user_address == user_address) {
                return i;
            }
        }
        return 0;
    }
    
    function get_user_number() public view returns(uint) {
        return users.length;
    }
    
    //Получить информацию о пользователе по его адресу - Работает
    function get_user_by_user_address(address user_address) public view returns(address, string memory, uint, uint, string memory) {
        for (uint i=0; i<users.length; i++) {
            if (users[i].user_address == user_address) {
                return(users[i].user_address, users[i].name, users[i].category, users[i].role, users[i].open_key);
            }
        }
    }
    
    //Получить информацию о пользователе по его номеру - Работает
    function get_user_by_user_id(uint user_id) public view returns(address, string memory, uint, uint, string memory) {
        return(users[user_id].user_address, users[user_id].name, users[user_id].category, users[user_id].role, users[user_id].open_key);
    }
    
    //Получить количество запросов - Работает
    function get_request_number() public view returns(uint) {
        return requests.length;
    }
    
    //Получить конкретный запрос
    function get_request_by_request_number(uint request_number) public view returns(address, uint, uint) {
        return(requests[request_number].user_address, requests[request_number].new_role, requests[request_number].new_category);
    }
    
    //Получить номер запроса новой роли по адресу пользователя и по указаной роли - Работает
    function get_role_request_id_by_user_address(address user_address, uint new_role) public view returns(uint) {
        for (uint i=0; i<requests.length; i++) {
            if (requests[i].user_address == user_address && requests[i].new_role == new_role) {
                return i;
            }
        }
    }
    
    //Получить номер запроса новой категории по адресу пользователя -
    function get_category_request_id_by_user_address(address user_address) public view returns(uint) {
        for (uint i=0; i<requests.length; i++) {
            if (requests[i].user_address == user_address && requests[i].new_category == 2) {
                return i;
            }
        }
    }
    
    
    
    //Регистрация в системе - Работает
    function check_in(string memory name, string memory open_key) public {
        uint user_id = get_user_id_by_user_address(msg.sender);
        if (user_id == 0) {
            users.push(User(msg.sender, name, 3, 3, open_key));
        }
        else {
            require(users[user_id].role != 0, "You'ra locked by admin");
            users[user_id].open_key = open_key;
            users[user_id].category = 3;
            users[user_id].role = 3;
        }
    }
    
    //Удаление из системы - Работает
    function delete_user(address user_address) public isAdmin {
        users[get_user_id_by_user_address(user_address)].role = 0;
    }
    
    //Запросить права администратора - Работает
    function request_admin_rights() public {
        uint user_id = get_user_id_by_user_address(msg.sender);
        require(users[user_id].role == 3, "This role can't be given to you");
        requests.push(Request(msg.sender, 1, 0));
    }
    
    //Запросить права библиотекаря - Работает
    function request_librarian_rights() public {
        uint user_id = get_user_id_by_user_address(msg.sender);
        require(users[user_id].role == 3, "This role can't be given to you");
        requests.push(Request(msg.sender, 2, 0));
    }
    
    //Установить новые права пользователю - Работает
    function confirm_rights(address user_address, uint new_role) public isAdmin {
        uint request_id = get_role_request_id_by_user_address(user_address, new_role);
        uint user_id = get_user_id_by_user_address(user_address);
        users[user_id].role = 2;
        delete requests[request_id];
    }
    
    //Отказать в установлении новых прав - Работает
    function refuse_rights(address user_address, uint new_role) public isAdmin {
        uint request_id = get_role_request_id_by_user_address(user_address, new_role);
        delete requests[request_id];
    }
    
    //Запросить доступ к категории 1 - Работает
    function request_access_to_other() public {
        uint user_id = get_user_id_by_user_address(msg.sender);
        require(users[user_id].category != 1, "You've alredy had this category");
        requests.push(Request(msg.sender, 0, 1));
    }
    
    //Разрешить доступ к первой категории - Работает
    function confirm_access_to_other(address user_address) public isAdmin {
        uint request_id = get_category_request_id_by_user_address(user_address);
        uint user_id = get_user_id_by_user_address(user_address);
        require(msg.sender != user_address, "You can give an access for othet files for youself");
        users[user_id].category = 1;
        delete(requests[request_id]);
    }
    
    //Отказать в доступе к первой категории - Работает
    function refuse_access_to_other(address user_address) public isAdmin {
        uint request_id = get_category_request_id_by_user_address(user_address);
        require(msg.sender != user_address, "You can refuse an access for othet files for youself");
        delete(requests[request_id]);
    }
    
    
    
    //Запрос на внесение общедоступного файла в архив
    function create_file_3(string memory title, uint tipe, string memory file_hash) public {
        uint user_id = get_user_id_by_user_address(msg.sender);
        string memory author = users[user_id].name;
        uint[] memory viewtime;
        address[] memory viewers;
        bool[] memory view_status;
        files.push(File(files.length, title, author, tipe, 3, 0, file_hash, viewtime, viewers, view_status, false));
    }
    
    //Разрешить опубликовать общедоступный файл
    function confirm_print_2(uint file_id) public isLibr {
        files[file_id].confirmed = true;
    }
    
    //Запретить публиковать общедоступный файл 
    function refuse_print_3(uint file_id) public isLibr {
        delete files[file_id];
    }
    
    //Занести файл первой категории в архив (прочая тайна)
    function create_file_1(string memory title, uint tipe, string memory file_hash) public isLibr {
        uint[] memory viewtime;
        address[] memory viewers;
        bool[] memory view_status;
        files.push(File(files.length, title, "", tipe, 1, 0, file_hash, viewtime, viewers, view_status, true));
    }
    
    //Запрос на внесение коммерческой тайны в архив (категория 2)
    function create_file_2(string memory title, uint tipe, uint period, string memory file_hash) public {
        uint user_id = get_user_id_by_user_address(msg.sender);
        string memory author = users[user_id].name;
        uint[] memory viewtime;
        address[] memory viewers;
        bool[] memory view_status;
        files.push(File(files.length, title, author, tipe, 2, period, file_hash, viewtime, viewers, view_status, false));
    }
    
    //Разрешить опубликовать коммерческую тайну
    function confirm_print_3(uint file_id) public isLibr {
        files[file_id].confirmed = true;
    }
}
