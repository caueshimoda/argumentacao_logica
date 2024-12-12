from tkinter import *


class App(Tk):

    def __init__(self):
        # Inicialização da janela.
        super().__init__()
        self.title('Argumentação Lógica')

        # Inicialização de variáveis relativas às proposições e aos widgets de caixas de combinação.
        self.padrao = 'Nenhuma proposição adicionada'
        self.proposicoes = [self.padrao]
        self.maximo = 10
        self.premissas = 2
        self.se1_str_var = StringVar()
        self.se1_str_var.set(self.proposicoes[0])
        self.se2_str_var = StringVar()
        self.se2_str_var.set(self.proposicoes[0])
        self.se3_str_var = StringVar()
        self.se3_str_var.set(self.proposicoes[0])
        self.se4_str_var = StringVar()
        self.se4_str_var.set(self.proposicoes[0])
        self.se5_str_var = StringVar()
        self.se5_str_var.set(self.proposicoes[0])
        self.entao1_str_var = StringVar()
        self.entao1_str_var.set(self.proposicoes[0])
        self.entao2_str_var = StringVar()
        self.entao2_str_var.set(self.proposicoes[0])
        self.entao3_str_var = StringVar()
        self.entao3_str_var.set(self.proposicoes[0])
        self.entao4_str_var = StringVar()
        self.entao4_str_var.set(self.proposicoes[0])
        self.entao5_str_var = StringVar()
        self.entao5_str_var.set(self.proposicoes[0])
        self.se_conclusao_var = StringVar()
        self.se_conclusao_var.set(self.proposicoes[0])
        self.entao_conclusao_var = StringVar()
        self.entao_conclusao_var.set(self.proposicoes[0])
        self.remover_str_var = StringVar()
        self.remover_str_var.set(self.proposicoes[0])
        self.padx = 5
        self.pady = 5

        # Inicialização de widgets que serão atualizados em funções
        self.cbo_se1 = OptionMenu(self, self.se1_str_var, *self.proposicoes)
        self.cbo_se2 = OptionMenu(self, self.se2_str_var, *self.proposicoes)
        self.cbo_se3 = OptionMenu(self, self.se3_str_var, *self.proposicoes)
        self.cbo_se4 = OptionMenu(self, self.se4_str_var, *self.proposicoes)
        self.cbo_se5 = OptionMenu(self, self.se5_str_var, *self.proposicoes)
        self.cbo_entao1 = OptionMenu(self, self.entao1_str_var, *self.proposicoes)
        self.cbo_entao2 = OptionMenu(self, self.entao2_str_var, *self.proposicoes)
        self.cbo_entao3 = OptionMenu(self, self.entao3_str_var, *self.proposicoes)
        self.cbo_entao4 = OptionMenu(self, self.entao4_str_var, *self.proposicoes)
        self.cbo_entao5 = OptionMenu(self, self.entao5_str_var, *self.proposicoes)
        self.cbo_se_conclusao = OptionMenu(self, self.se_conclusao_var, *self.proposicoes)
        self.cbo_entao_conclusao = OptionMenu(self, self.entao_conclusao_var, *self.proposicoes)
        self.cbo_remover = OptionMenu(self, self.remover_str_var, *self.proposicoes)
        self.lbl_total = Label(self, text=f'Proposições adicionadas: 0. Máximo: {self.maximo}')
        self.btn_concluir = Button(self, text='Checar validade', state='disabled')
        self.btn_add = Button(self, text='Adicionar')
        self.lbl_validade = Label(self, text='')

    def validar_conclusao(self):
        # Habilita ou desabilita o botão de concluir (pelo menos uma proposição deve ser adicionada para habilitar).
        if self.proposicoes[0] != self.padrao:
            self.btn_concluir['state'] = 'normal'
        else:
            self.btn_concluir['state'] = 'disabled'

    def atualizar_cbos(self):
        # Atualiza todas as caixas de combinação com os valores da lista de proposições.
        self.cbo_se1['menu'].delete(0, 'end')
        for op in self.proposicoes:
            self.cbo_se1['menu'].add_command(label=op, command=lambda valor=op: self.se1_str_var.set(valor))
        self.se1_str_var.set(self.proposicoes[0])

        self.cbo_se2['menu'].delete(0, 'end')
        for op in self.proposicoes:
            self.cbo_se2['menu'].add_command(label=op, command=lambda valor=op: self.se2_str_var.set(valor))
        self.se2_str_var.set(self.proposicoes[0])

        self.cbo_se3['menu'].delete(0, 'end')
        for op in self.proposicoes:
            self.cbo_se3['menu'].add_command(label=op, command=lambda valor=op: self.se3_str_var.set(valor))
        self.se3_str_var.set(self.proposicoes[0])

        self.cbo_se4['menu'].delete(0, 'end')
        for op in self.proposicoes:
            self.cbo_se4['menu'].add_command(label=op, command=lambda valor=op: self.se4_str_var.set(valor))
        self.se4_str_var.set(self.proposicoes[0])

        self.cbo_se5['menu'].delete(0, 'end')
        for op in self.proposicoes:
            self.cbo_se5['menu'].add_command(label=op, command=lambda valor=op: self.se5_str_var.set(valor))
        self.se5_str_var.set(self.proposicoes[0])

        self.cbo_entao1['menu'].delete(0, 'end')
        for op in self.proposicoes:
            self.cbo_entao1['menu'].add_command(label=op, command=lambda valor=op: self.entao1_str_var.set(valor))
        self.entao1_str_var.set(self.proposicoes[0])

        self.cbo_entao2['menu'].delete(0, 'end')
        for op in self.proposicoes:
            self.cbo_entao2['menu'].add_command(label=op, command=lambda valor=op: self.entao2_str_var.set(valor))
        self.entao2_str_var.set(self.proposicoes[0])

        self.cbo_entao3['menu'].delete(0, 'end')
        for op in self.proposicoes:
            self.cbo_entao3['menu'].add_command(label=op, command=lambda valor=op: self.entao3_str_var.set(valor))
        self.entao3_str_var.set(self.proposicoes[0])

        self.cbo_entao4['menu'].delete(0, 'end')
        for op in self.proposicoes:
            self.cbo_entao4['menu'].add_command(label=op, command=lambda valor=op: self.entao4_str_var.set(valor))
        self.entao4_str_var.set(self.proposicoes[0])

        self.cbo_entao5['menu'].delete(0, 'end')
        for op in self.proposicoes:
            self.cbo_entao5['menu'].add_command(label=op, command=lambda valor=op: self.entao5_str_var.set(valor))
        self.entao5_str_var.set(self.proposicoes[0])

        self.cbo_se_conclusao['menu'].delete(0, 'end')
        for op in self.proposicoes:
            self.cbo_se_conclusao['menu'].add_command(label=op,
                                                      command=lambda valor=op: self.se_conclusao_var.set(valor))
        self.se_conclusao_var.set(self.proposicoes[0])

        self.cbo_entao_conclusao['menu'].delete(0, 'end')
        for op in self.proposicoes:
            self.cbo_entao_conclusao['menu'].add_command(label=op,
                                                         command=lambda valor=op: self.entao_conclusao_var.set(valor))
        self.entao_conclusao_var.set(self.proposicoes[0])

        self.cbo_remover['menu'].delete(0, 'end')
        for op in self.proposicoes:
            self.cbo_remover['menu'].add_command(label=op, command=lambda valor=op: self.remover_str_var.set(valor))
        self.remover_str_var.set(self.proposicoes[0])

    def atualizar_total(self):
        # Atualiza o label que avisa quantas proposições foram adicionadas e o limite de adições.
        atual = len(self.proposicoes)
        if self.proposicoes[0] == self.padrao:
            atual = 0
        self.lbl_total.configure(text=f'Proposições adicionadas: {atual}. Máximo: {self.maximo}')

    def adicionar_proposicao(self, p):
        # Adiciona uma proposição à lista caso não seja repetida. Adiciona também sua negação.
        if p and p not in self.proposicoes:
            if self.proposicoes[0] == self.padrao:
                self.proposicoes[0] = p
            else:
                self.proposicoes.append(p)
            self.proposicoes.append(f'Não {p}')
            self.atualizar_total()
            self.atualizar_cbos()
            self.validar_conclusao()
            if len(self.proposicoes) == self.maximo:
                self.btn_add['state'] = 'disabled'

    def remover_proposicao(self, p):
        # Remove uma proposição e sua negação da lista.
        if p != self.padrao:
            self.proposicoes.remove(p)
            if f'Não {p}' in self.proposicoes:
                self.proposicoes.remove(f'Não {p}')
            elif p[4:] in self.proposicoes:
                self.proposicoes.remove(p[4:])
            if len(self.proposicoes) == 0:
                self.proposicoes.append(self.padrao)
            self.atualizar_total()
            self.atualizar_cbos()
            self.validar_conclusao()
            self.btn_add['state'] = 'normal'

    def adicionar_premissa(self):
        # Limpa a janela e adiciona uma linha de premissa
        self.premissas += 1
        for widget in self.winfo_children():
            widget.grid_forget()
        self.desenhar_janela()

    def remover_premissa(self):
        # Limpa a janela e remove uma linha de premissa
        self.premissas -= 1
        for widget in self.winfo_children():
            widget.grid_forget()
        self.desenhar_janela()

    def concluir(self):
        # Avalia a validade da conclusão.
        validade = ''
        mudanca = False

        '''Estrutura dos argumentos: a chave "proposição" carrega a valor que está em cada 
        caixa de combinação, escolhido pelo usuário.
        A chave "premissa" carrega o número da premissa em que está o argumento, sendo que 
        a premissa número 6 é a conclusão.
        A chave "tipo" diz se a proposição está na posição "se" ou "então".
        A chave "valor" diz se a proposição é verdadeira ou falsa.'''
        argumentos = [{'proposicao': self.se1_str_var.get(), 'premissa': 1, 'tipo': 'se', 'valor': ''},
                      {'proposicao': self.entao1_str_var.get(), 'premissa': 1, 'tipo': 'entao', 'valor': ''},
                      {'proposicao': self.se2_str_var.get(), 'premissa': 2, 'tipo': 'se', 'valor': ''},
                      {'proposicao': self.entao2_str_var.get(), 'premissa': 2, 'tipo': 'entao', 'valor': ''}]
        if self.premissas > 2:
            argumentos.append({'proposicao': self.se3_str_var.get(), 'premissa': 3, 'tipo': 'se', 'valor': ''})
            argumentos.append(
                {'proposicao': self.entao3_str_var.get(), 'premissa': 3, 'tipo': 'entao', 'valor': ''})
        if self.premissas > 3:
            argumentos.append({'proposicao': self.se4_str_var.get(), 'premissa': 4, 'tipo': 'se', 'valor': ''})
            argumentos.append(
                {'proposicao': self.entao4_str_var.get(), 'premissa': 4, 'tipo': 'entao', 'valor': ''})
        if self.premissas > 4:
            argumentos.append({'proposicao': self.se5_str_var.get(), 'premissa': 5, 'tipo': 'se', 'valor': ''})
            argumentos.append(
                {'proposicao': self.entao5_str_var.get(), 'premissa': 5, 'tipo': 'entao', 'valor': ''})

        '''A única proposição que já carrega de saída um valor verdadeiro é o "se" da conclusão,
        de acordo com a equivalência logica P -> (Q -> R) <=> (P && Q) -> R.'''
        argumentos.append(
            {'proposicao': self.se_conclusao_var.get(), 'premissa': 6, 'tipo': 'se', 'valor': 'verdade'})
        argumentos.append(
            {'proposicao': self.entao_conclusao_var.get(), 'premissa': 6, 'tipo': 'entao', 'valor': ''})
        conclusao = self.entao_conclusao_var.get()

        '''Antes de realizar a avaliação, o programa checa se há alguma contradição em uma premissa,
        ou seja, P -> Não P.'''
        for i in range(0, len(argumentos), 2):
            if ((argumentos[i + 1]['proposicao'] == f'Não {argumentos[i]['proposicao']}') or
                    (argumentos[i]['proposicao'][:4] == 'Não ' and
                     argumentos[i]['proposicao'][4:] == argumentos[i + 1]['proposicao'])):
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

        self.lbl_validade.configure(text=validade)

    def validar_txt(self, nova):
        # Regula a entrada da caixa de texto, limitando a quantidade de caracteres.
        if len(nova) > 20:
            return False
        return True

    def desenhar_linha(self, widgets, lin):
        for i in range(len(widgets)):
            widgets[i].grid(row=lin, column=i, sticky='W', padx=self.padx, pady=self.pady)

    def desenhar_janela(self):
        # Desenha a janela de acordo com o número de premissas atual (mínimo: 2 premissas, máximo: 5).
        linha = 0

        # Linha de widgets para a adição de proposições.
        lbl_prop = Label(self, text='Proposição:')
        txt_prop = Entry(self, width=30, validate='key', validatecommand=(self.register(self.validar_txt), '%P'))
        self.btn_add['command'] = lambda: self.adicionar_proposicao(txt_prop.get())
        lbl_remover = Label(self, text='Remover proposição:')
        btn_remover = Button(self, text='Remover', command=lambda: self.remover_proposicao(self.remover_str_var.get()))
        linha_widgets = [lbl_prop, txt_prop, self.btn_add, lbl_remover, self.cbo_remover, btn_remover]
        self.desenhar_linha(linha_widgets, linha)

        linha += 1

        self.lbl_total.grid(row=linha, column=0, sticky='W', padx=self.padx, pady=self.pady)

        linha += 1

        # Primeira linha  de widgets para a definição de premissas.
        lbl_se1 = Label(self, text='Se')
        lbl_entao1 = Label(self, text='Então')
        linha_widgets = [lbl_se1, self.cbo_se1, lbl_entao1, self.cbo_entao1]
        self.desenhar_linha(linha_widgets, linha)

        linha += 1

        # Segunda linha  de widgets para a definição de premissas.
        lbl_se2 = Label(self, text='Se')
        lbl_entao2 = Label(self, text='Então')
        linha_widgets = [lbl_se2, self.cbo_se2, lbl_entao2, self.cbo_entao2]
        self.desenhar_linha(linha_widgets, linha)

        linha += 1

        if self.premissas > 2:
            # Terceira linha  de widgets para a definição de premissas.
            lbl_se3 = Label(self, text='Se')
            lbl_entao3 = Label(self, text='Então')
            linha_widgets = [lbl_se3, self.cbo_se3, lbl_entao3, self.cbo_entao3]
            self.desenhar_linha(linha_widgets, linha)

            linha += 1

        if self.premissas > 3:
            # Quarta linha  de widgets para a definição de premissas.
            lbl_se4 = Label(self, text='Se')
            lbl_entao4 = Label(self, text='Então')
            linha_widgets = [lbl_se4, self.cbo_se4, lbl_entao4, self.cbo_entao4]
            self.desenhar_linha(linha_widgets, linha)

            linha += 1

        if self.premissas > 4:
            # Quinta linha  de widgets para a definição de premissas.
            lbl_se5 = Label(self, text='Se')
            lbl_entao5 = Label(self, text='Então')
            linha_widgets = [lbl_se5, self.cbo_se5, lbl_entao5, self.cbo_entao5]
            self.desenhar_linha(linha_widgets, linha)

            linha += 1

        if self.premissas < 5:
            btn_add_prem = Button(self, text='Adicionar premissa', command=self.adicionar_premissa)
            btn_add_prem.grid(row=linha, column=0, sticky='W', padx=self.padx, pady=self.pady)

        if self.premissas > 2:
            btn_remover_prem = Button(self, text='Remover premissa', command=self.remover_premissa)
            btn_remover_prem.grid(row=linha, column=1, sticky='W', padx=self.padx, pady=self.pady)

        linha += 1

        lbl_conclusao = Label(self, text='Conclusão:')
        lbl_conclusao.grid(row=linha, column=0, sticky='W', padx=self.padx, pady=self.pady)

        linha += 1

        # Linha da conclusão
        lbl_se_conc = Label(self, text='Se')
        lbl_entao_conc = Label(self, text='Então')
        linha_widgets = [lbl_se_conc, self.cbo_se_conclusao, lbl_entao_conc, self.cbo_entao_conclusao]
        self.desenhar_linha(linha_widgets, linha)

        linha += 1
        self.btn_concluir['command'] = self.concluir
        self.btn_concluir.grid(row=linha, column=0, sticky='W', padx=self.padx, pady=self.pady)

        linha += 1

        self.lbl_validade.grid(row=linha, column=0, sticky='W', padx=self.padx, pady=self.pady)


app = App()
app.desenhar_janela()
app.mainloop()
