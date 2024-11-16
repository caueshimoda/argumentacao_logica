from tkinter import *

# Inicialização da janela.
raiz = Tk()
raiz.title('Argumentação Lógica')

# Inicialização de variáveis relativas às proposições e aos widgets de caixas de combinação.
padrao = 'Nenhuma proposição adicionada'
proposicoes = [padrao]
maximo = 10
premissas = 2
se1_str_var = StringVar()
se1_str_var.set(proposicoes[0])
se2_str_var = StringVar()
se2_str_var.set(proposicoes[0])
se3_str_var = StringVar()
se3_str_var.set(proposicoes[0])
se4_str_var = StringVar()
se4_str_var.set(proposicoes[0])
se5_str_var = StringVar()
se5_str_var.set(proposicoes[0])
entao1_str_var = StringVar()
entao1_str_var.set(proposicoes[0])
entao2_str_var = StringVar()
entao2_str_var.set(proposicoes[0])
entao3_str_var = StringVar()
entao3_str_var.set(proposicoes[0])
entao4_str_var = StringVar()
entao4_str_var.set(proposicoes[0])
entao5_str_var = StringVar()
entao5_str_var.set(proposicoes[0])
se_conclusao_var = StringVar()
se_conclusao_var.set(proposicoes[0])
entao_conclusao_var = StringVar()
entao_conclusao_var.set(proposicoes[0])
remover_str_var = StringVar()
remover_str_var.set(proposicoes[0])

# Inicialização de widgets que serão atualizados em funções
cbo_se1 = OptionMenu(raiz, se1_str_var, *proposicoes)
cbo_se2 = OptionMenu(raiz, se2_str_var, *proposicoes)
cbo_se3 = OptionMenu(raiz, se3_str_var, *proposicoes)
cbo_se4 = OptionMenu(raiz, se4_str_var, *proposicoes)
cbo_se5 = OptionMenu(raiz, se5_str_var, *proposicoes)
cbo_entao1 = OptionMenu(raiz, entao1_str_var, *proposicoes)
cbo_entao2 = OptionMenu(raiz, entao2_str_var, *proposicoes)
cbo_entao3 = OptionMenu(raiz, entao3_str_var, *proposicoes)
cbo_entao4 = OptionMenu(raiz, entao4_str_var, *proposicoes)
cbo_entao5 = OptionMenu(raiz, entao5_str_var, *proposicoes)
cbo_se_conclusao = OptionMenu(raiz, se_conclusao_var, *proposicoes)
cbo_entao_conclusao = OptionMenu(raiz, entao_conclusao_var, *proposicoes)
cbo_remover = OptionMenu(raiz, remover_str_var, *proposicoes)
lbl_total = Label(raiz, text=f'Proposições adicionadas: 0. Máximo: {maximo}')
btn_concluir = Button(raiz, text='Checar validade', state='disabled')
btn_add = Button(raiz, text='Adicionar')
lbl_validade = Label(raiz, text='')


def validar_conclusao():
    # Habilita ou desabilita o botão de concluir (pelo menos uma proposição deve ser adicionada para habilitar).
    if proposicoes[0] != padrao:
        btn_concluir['state'] = 'normal'
    else:
        btn_concluir['state'] = 'disabled'


def atualizar_cbos():
    # Atualiza todas as caixas de combinação com os valores da lista de proposições.
    cbo_se1['menu'].delete(0, 'end')
    for op in proposicoes:
        cbo_se1['menu'].add_command(label=op, command=lambda valor=op: se1_str_var.set(valor))
    se1_str_var.set(proposicoes[0])

    cbo_se2['menu'].delete(0, 'end')
    for op in proposicoes:
        cbo_se2['menu'].add_command(label=op, command=lambda valor=op: se2_str_var.set(valor))
    se2_str_var.set(proposicoes[0])

    cbo_se3['menu'].delete(0, 'end')
    for op in proposicoes:
        cbo_se3['menu'].add_command(label=op, command=lambda valor=op: se3_str_var.set(valor))
    se3_str_var.set(proposicoes[0])

    cbo_se4['menu'].delete(0, 'end')
    for op in proposicoes:
        cbo_se4['menu'].add_command(label=op, command=lambda valor=op: se4_str_var.set(valor))
    se4_str_var.set(proposicoes[0])

    cbo_se5['menu'].delete(0, 'end')
    for op in proposicoes:
        cbo_se5['menu'].add_command(label=op, command=lambda valor=op: se5_str_var.set(valor))
    se5_str_var.set(proposicoes[0])

    cbo_entao1['menu'].delete(0, 'end')
    for op in proposicoes:
        cbo_entao1['menu'].add_command(label=op, command=lambda valor=op: entao1_str_var.set(valor))
    entao1_str_var.set(proposicoes[0])

    cbo_entao2['menu'].delete(0, 'end')
    for op in proposicoes:
        cbo_entao2['menu'].add_command(label=op, command=lambda valor=op: entao2_str_var.set(valor))
    entao2_str_var.set(proposicoes[0])

    cbo_entao3['menu'].delete(0, 'end')
    for op in proposicoes:
        cbo_entao3['menu'].add_command(label=op, command=lambda valor=op: entao3_str_var.set(valor))
    entao3_str_var.set(proposicoes[0])

    cbo_entao4['menu'].delete(0, 'end')
    for op in proposicoes:
        cbo_entao4['menu'].add_command(label=op, command=lambda valor=op: entao4_str_var.set(valor))
    entao4_str_var.set(proposicoes[0])

    cbo_entao5['menu'].delete(0, 'end')
    for op in proposicoes:
        cbo_entao5['menu'].add_command(label=op, command=lambda valor=op: entao5_str_var.set(valor))
    entao5_str_var.set(proposicoes[0])

    cbo_se_conclusao['menu'].delete(0, 'end')
    for op in proposicoes:
        cbo_se_conclusao['menu'].add_command(label=op, command=lambda valor=op: se_conclusao_var.set(valor))
    se_conclusao_var.set(proposicoes[0])

    cbo_entao_conclusao['menu'].delete(0, 'end')
    for op in proposicoes:
        cbo_entao_conclusao['menu'].add_command(label=op, command=lambda valor=op: entao_conclusao_var.set(valor))
    entao_conclusao_var.set(proposicoes[0])

    cbo_remover['menu'].delete(0, 'end')
    for op in proposicoes:
        cbo_remover['menu'].add_command(label=op, command=lambda valor=op: remover_str_var.set(valor))
    remover_str_var.set(proposicoes[0])


def atualizar_total():
    # Atualiza o label que avisa quantas proposições foram adicionadas e o limite de adições.
    atual = len(proposicoes)
    if proposicoes[0] == padrao:
        atual = 0
    lbl_total.configure(text=f'Proposições adicionadas: {atual}. Máximo: {maximo}')


def adicionar_proposicao(p):
    # Adiciona uma proposição à lista caso não seja repetida. Adiciona também sua negação.
    if p and p not in proposicoes:
        if proposicoes[0] == padrao:
            proposicoes[0] = p
        else:
            proposicoes.append(p)
        proposicoes.append(f'Não {p}')
        atualizar_total()
        atualizar_cbos()
        validar_conclusao()
        if len(proposicoes) == maximo:
            btn_add['state'] = 'disabled'


def remover_proposicao(p):
    # Remove uma proposição e sua negação da lista.
    if p != padrao:
        proposicoes.remove(p)
        if f'Não {p}' in proposicoes:
            proposicoes.remove(f'Não {p}')
        elif p[4:] in proposicoes:
            proposicoes.remove(p[4:])
        if len(proposicoes) == 0:
            proposicoes.append(padrao)
        atualizar_total()
        atualizar_cbos()
        validar_conclusao()
        btn_add['state'] = 'normal'


def adicionar_premissa():
    # Limpa a janela e adiciona uma linha de premissa
    global premissas
    premissas += 1
    for widget in raiz.winfo_children():
        widget.grid_forget()
    desenhar_janela(premissas)


def remover_premissa():
    # Limpa a janela e remove uma linha de premissa
    global premissas
    premissas -= 1
    for widget in raiz.winfo_children():
        widget.grid_forget()
    desenhar_janela(premissas)


def concluir():
    # Avalia a validade da conclusão.
    global premissas
    validade = ''
    mudanca = False

    '''Estrutura dos argumentos: a chave "proposição" carrega a valor que está em cada 
    caixa de combinação, escolhido pelo usuário.
    A chave "premissa" carrega o número da premissa em que está o argumento, sendo que 
    a premissa número 6 é a conclusão.
    A chave "tipo" diz se a proposição está na posição "se" ou "então".
    A chave "valor" diz se a proposição é verdadeira ou falsa.'''
    argumentos = [{'proposicao': se1_str_var.get(), 'premissa': 1, 'tipo': 'se', 'valor': ''},
                  {'proposicao': entao1_str_var.get(), 'premissa': 1, 'tipo': 'entao', 'valor': ''},
                  {'proposicao': se2_str_var.get(), 'premissa': 2, 'tipo': 'se', 'valor': ''},
                  {'proposicao': entao2_str_var.get(), 'premissa': 2, 'tipo': 'entao', 'valor': ''}]
    if premissas > 2:
        argumentos.append({'proposicao': se3_str_var.get(), 'premissa': 3, 'tipo': 'se', 'valor': ''})
        argumentos.append({'proposicao': entao3_str_var.get(), 'premissa': 3, 'tipo': 'entao', 'valor': ''})
    if premissas > 3:
        argumentos.append({'proposicao': se4_str_var.get(), 'premissa': 4, 'tipo': 'se', 'valor': ''})
        argumentos.append({'proposicao': entao4_str_var.get(), 'premissa': 4, 'tipo': 'entao', 'valor': ''})
    if premissas > 4:
        argumentos.append({'proposicao': se5_str_var.get(), 'premissa': 5, 'tipo': 'se', 'valor': ''})
        argumentos.append({'proposicao': entao5_str_var.get(), 'premissa': 5, 'tipo': 'entao', 'valor': ''})

    '''A única proposição que já carrega de saída um valor verdadeiro é o "se" da conclusão,
    de acordo com a equivalência logica P -> (Q -> R) <=> (P && Q) -> R.'''
    argumentos.append({'proposicao': se_conclusao_var.get(), 'premissa': 6, 'tipo': 'se', 'valor': 'verdade'})
    argumentos.append({'proposicao': entao_conclusao_var.get(), 'premissa': 6, 'tipo': 'entao', 'valor': ''})
    conclusao = entao_conclusao_var.get()

    '''Antes de realizar a avaliação, o programa checa se há alguma contradição em uma premissa,
    ou seja, P -> Não P.'''
    for i in range(0, len(argumentos), 2):
        if ((argumentos[i+1]['proposicao'] == f'Não {argumentos[i]['proposicao']}') or
                (argumentos[i]['proposicao'][:4] == 'Não ' and
                 argumentos[i]['proposicao'][4:] == argumentos[i+1]['proposicao'])):
            '''Se o número da premissa for 6, trata-se da conclusão.'''
            if argumentos[i]['premissa'] == 6:
                validade = 'A conclusão é uma falácia (contradição)'
            else:
                validade = f'Há uma contradição na premissa {argumentos[i]['premissa']}'
            break

    while not validade:
        for argumento in argumentos:
            '''Primeiro o algoritmo checa se o argumento já tem um valor definido, e se 
            a proposição é a mesma do "então" do argumento conclusivo. Nesse caso, a avaliação
            acabou e a validade pode ser determinada.'''
            if argumento['valor']:
                if argumento['proposicao'] == conclusao:
                    if argumento['valor'] == 'verdade':
                        validade = 'A conclusão é válida'
                    else:
                        validade = 'A conclusão é uma falácia (contradição)'
                    mudanca = True
                else:
                    '''Não sendo a proposição da conclusão, a função compara o argumento atual
                    com todos os outros argumentos da lista, chamados individualmente de 
                    "argumento_2", e muda o valor da proposição sempre que possível.'''
                    for argumento_2 in argumentos:
                        if not argumento_2['valor']:
                            if argumento_2['proposicao'] == argumento['proposicao']:
                                '''Quando as proposições são iguais, a função atribui o mesmo
                                valor para o argumento_2.'''
                                argumento_2['valor'] = argumento['valor']
                                mudanca = True
                            elif ((argumento_2['proposicao'] == f'Não {argumento['proposicao']}') or
                                  (argumento['proposicao'][:4] == 'Não '
                                   and argumento['proposicao'][4:] == argumento_2['proposicao'])):
                                '''Quando uma proposição é a negação da outra, a função atribui 
                                o valor oposto para o argumento_2.'''
                                if argumento['valor'] == 'verdade':
                                    argumento_2['valor'] = 'falso'
                                else:
                                    argumento_2['valor'] = 'verdade'
                                mudanca = True
                            elif (argumento['tipo'] == 'entao' and argumento['valor'] == 'falso'
                                  and argumento['premissa'] == argumento_2['premissa']):
                                '''Caso o tipo da proposição 1 seja "então" e ela for falsa, se o número
                                da premissa dos dois argumentos for o mesmo quer dizer que a proposição 2
                                necessariamente é falsa, já que um "se" verdadeiro na premissa não pode gerar 
                                um "então" falso.'''
                                argumento_2['valor'] = 'falso'
                                mudanca = True
                            elif ((argumento['tipo'] == 'se' and argumento['valor'] == 'verdade'
                                  and argumento['premissa'] == argumento_2['premissa'])
                                  and argumento['premissa'] != 6):
                                '''Por fim, como um "se" verdadeiro nunca gera em "então" falso na premissa,
                                a proposição 2 deve ser verdadeira caso a primeira seja do tipo "se" 
                                e verdadeira, a não ser que se trate da conclusão (número 6), pois não 
                                sabemos ainda se ela é necessariamente verdadeira.'''
                                argumento_2['valor'] = 'verdade'
                                mudanca = True

        if not mudanca:
            '''Se nenhum valor de argumento foi alterado durante o laço, quer dizer que 
            nada mais se pode dizer sobre a conclusão, portanto ela não é necessariamente
            falsa nem verdadeira, sendo uma falácia por contingência.'''
            validade = 'A conclusão é uma falácia (contingência)'
        else:
            mudanca = False

    lbl_validade.configure(text=validade)


def validar_txt(nova):
    # Regula a entrada da caixa de texto, limitando a quantidade de caracteres.
    if len(nova) > 20:
        return False
    return True


padx = 5
pady = 5


def desenhar_janela(prem):
    # Desenha a janela de acordo com o número de premissas atual (mínimo: 2 premissas, máximo: 5).
    linha = 0

    # Linha de widgets para a adição de proposições.
    lbl_prop = Label(raiz, text='Proposição:')
    txt_prop = Entry(raiz, width=30, validate='key', validatecommand=(raiz.register(validar_txt), '%P'))
    btn_add['command'] = lambda: adicionar_proposicao(txt_prop.get())
    lbl_remover = Label(raiz, text='Remover proposição:')
    btn_remover = Button(raiz, text='Remover', command=lambda: remover_proposicao(remover_str_var.get()))
    linha_widgets = [lbl_prop, txt_prop, btn_add, lbl_remover, cbo_remover, btn_remover]
    for i in range(len(linha_widgets)):
        linha_widgets[i].grid(row=linha, column=i, sticky='W', padx=padx, pady=pady)

    linha += 1

    lbl_total.grid(row=linha, column=0, sticky='W', padx=padx, pady=pady)

    linha += 1

    # Primeira linha  de widgets para a definição de premissas.
    lbl_se1 = Label(raiz, text='Se')
    lbl_entao1 = Label(raiz, text='Então')
    linha_widgets = [lbl_se1, cbo_se1, lbl_entao1, cbo_entao1]
    for i in range(len(linha_widgets)):
        linha_widgets[i].grid(row=linha, column=i, sticky='W', padx=padx, pady=pady)

    linha += 1

    # Segunda linha  de widgets para a definição de premissas.
    lbl_se2 = Label(raiz, text='Se')
    lbl_entao2 = Label(raiz, text='Então')
    linha_widgets = [lbl_se2, cbo_se2, lbl_entao2, cbo_entao2]
    for i in range(len(linha_widgets)):
        linha_widgets[i].grid(row=linha, column=i, sticky='W', padx=padx, pady=pady)

    linha += 1

    if prem > 2:
        # Terceira linha  de widgets para a definição de premissas.
        lbl_se3 = Label(raiz, text='Se')
        lbl_entao3 = Label(raiz, text='Então')
        linha_widgets = [lbl_se3, cbo_se3, lbl_entao3, cbo_entao3]
        for i in range(len(linha_widgets)):
            linha_widgets[i].grid(row=linha, column=i, sticky='W', padx=padx, pady=pady)

        linha += 1

    if prem > 3:
        # Quarta linha  de widgets para a definição de premissas.
        lbl_se4 = Label(raiz, text='Se')
        lbl_entao4 = Label(raiz, text='Então')
        linha_widgets = [lbl_se4, cbo_se4, lbl_entao4, cbo_entao4]
        for i in range(len(linha_widgets)):
            linha_widgets[i].grid(row=linha, column=i, sticky='W', padx=padx, pady=pady)

        linha += 1

    if prem > 4:
        # Quinta linha  de widgets para a definição de premissas.
        lbl_se5 = Label(raiz, text='Se')
        lbl_entao5 = Label(raiz, text='Então')
        linha_widgets = [lbl_se5, cbo_se5, lbl_entao5, cbo_entao5]
        for i in range(len(linha_widgets)):
            linha_widgets[i].grid(row=linha, column=i, sticky='W', padx=padx, pady=pady)

        linha += 1

    if prem < 5:
        btn_add_prem = Button(raiz, text='Adicionar premissa', command=adicionar_premissa)
        btn_add_prem.grid(row=linha, column=0, sticky='W', padx=padx, pady=pady)

    if prem > 2:
        btn_remover_prem = Button(raiz, text='Remover premissa', command=remover_premissa)
        btn_remover_prem.grid(row=linha, column=1, sticky='W', padx=padx, pady=pady)

    linha += 1

    lbl_conclusao = Label(raiz, text='Conclusão:')
    lbl_conclusao.grid(row=linha, column=0, sticky='W', padx=padx, pady=pady)

    linha += 1

    # Linha da conclusão
    lbl_se_conc = Label(raiz, text='Se')
    lbl_entao_conc = Label(raiz, text='Então')
    linha_widgets = [lbl_se_conc, cbo_se_conclusao, lbl_entao_conc, cbo_entao_conclusao]
    for i in range(len(linha_widgets)):
        linha_widgets[i].grid(row=linha, column=i, sticky='W', padx=padx, pady=pady)

    linha += 1
    btn_concluir['command'] = concluir
    btn_concluir.grid(row=linha, column=0, sticky='W', padx=padx, pady=pady)

    linha += 1

    lbl_validade.grid(row=linha, column=0, sticky='W', padx=padx, pady=pady)


desenhar_janela(premissas)
raiz.mainloop()
