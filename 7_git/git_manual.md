# Доступ в GitHub

### Linux

1. **Генерация SSH-ключа**

   - Откройте терминал.
   - Введите следующую команду и следуйте инструкциям:
     ```bash
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
     ```
   - По умолчанию ключ сохраняется в файле `~/.ssh/id_rsa`.

2. **Добавление SSH-ключа к ssh-agent**

   - Запустите SSH-агент:
     ```bash
     eval "$(ssh-agent -s)"
     ```
   - Добавьте ключ в агент:
     ```bash
     ssh-add ~/.ssh/id_rsa
     ```
   
3. **Добавление SSH-ключа на GitHub**
   
   - Выведите содержимое ключа в терминале:
     ```bash
     cat ~/.ssh/id_rsa.pub
     ```
   - Скопируйте # Доступ в GitHub

4. **Клонирование репозитория через SSH**

   При клонировании репозитория используйте SSH-URL:
   ```bash
   git clone git@github.com:username/repo.git
   ```
   вывод команды.
   - Откройте GitHub, перейдите в "Settings" → "SSH and GPG keys" → "New SSH key".
   - Вставьте ключ и дайте ему название.
   