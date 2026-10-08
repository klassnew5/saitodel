path = 'index.html'
html = open(path, encoding='utf-8').read()

old = 'Базовый лендинг — <span class="highlight">2 дня</span>. Стандартный — <span class="highlight">от 5 дней</span>. Сложный проект — срок обсуждается.'
new = 'Базовый лендинг — <span class="highlight">2 дня</span> при готовых материалах (текст, фото, логотип). Стандартный — <span class="highlight">от 5 дней</span>. Сложный проект — срок обсуждается. Доработки и правки сверх пакета — <span class="highlight">5 000 ₽/час</span>.'

if old in html:
    html = html.replace(old, new, 1)
    open(path, 'w', encoding='utf-8').write(html)
    print('✅ HTML обновлён')
else:
    print('⚠️ Не найдено — правь вручную')
