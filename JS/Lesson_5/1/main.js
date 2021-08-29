let field = document.createElement('DIV');
document.body.appendChild(field);

for (let y = 0; y < 10; y++) {
    for (let x = 0; x < 10; x++) {
        let css = x ? {} : { clear: 'left' };
        let content = '';
        if (y == 0 || y == 9)
            content = x > 0 && x < 9 ? 'ABCDEFGH'.charAt(x - 1) : null;
        else if (x == 0 || x == 9)
            content = 9 - y;
        else css.background = (x + y) % 2 ? '#000' : '#fff';

        let node = document.createElement('DIV');
        css.width = '50px';
        css.height = css.width;
        css.textAlign = 'center';
	css.lineHeight = '50px'
        css.float = 'left';
        for (let i in css) node.style[i] = css[i];
        if (content)
            node.innerHTML = content;
        field.appendChild(node);
    }
}
