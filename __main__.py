from tkinter import *
from tkinter import ttk

from modules.conector import interface_db

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser


pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))


vList=[]
pList=[]





root = Tk()


class Relatorios():
    def printRelatorio(self):
        webbrowser.open("relatorio.pdf")

    def geraRelatBalanco(self):
        self.c = canvas.Canvas("relatorio.pdf")

         
        result= self.interface_banco.getTotalVendas()
        print(result)

        self.c.setFont("VeraBd",16)
        self.c.drawString(200, 790, 'Balanço do mês')

        self.c.setFont("VeraBd",12)
        self.c.drawString(60, 700, '°Novembro ')
        self.c.setFont("Vera",10)
        self.c.drawString(150, 700, "USD "+str(result))
        self.c.rect(20, 550, 550, 5, fill=True, stroke=False)

        self.c.showPage()
        self.c.save()
        self.printRelatorio()



    def geraRelatMaiorVenda(self):
        self.c = canvas.Canvas("relatorio.pdf")

         
        result= self.interface_banco.getFuncionarioMaiorValor()
        print(result)
        self.c.setFont("VeraBd",16)
        self.c.drawString(180, 790, 'Relatório de Vendedores')
        y=700
        for i in result:
            self.c.setFont("VeraBd",10)
            self.c.drawString(60, y, '°Vendedor: ')
            self.c.setFont("Vera",8)
            self.c.drawString(140, y, str(i[0]))

            self.c.setFont("VeraBd",10)
            self.c.drawString(320, y, '°Entrada: ')
            self.c.setFont("Vera",8)
            self.c.drawString(380, y, str(i[1]))
            
            y-=50
            self.c.rect(20, y, 550, 5, fill=True, stroke=False)
            y-=50

        self.c.showPage()
        self.c.save()
        self.printRelatorio()

    def geraRelatMaiorQuant(self):
        self.c = canvas.Canvas("relatorio.pdf")

         
        result= self.interface_banco.getFuncionarioMaisVendas()
        print(result)
        self.c.setFont("VeraBd",16)
        self.c.drawString(180, 790, 'Relatório de Vendedores')
        y=700
        for i in result:
            self.c.setFont("VeraBd",10)
            self.c.drawString(60, y, '°Vendedor: ')
            self.c.setFont("Vera",8)
            self.c.drawString(140, y, str(i[0]))

            self.c.setFont("VeraBd",10)
            self.c.drawString(320, y, '°Entrada: ')
            self.c.setFont("Vera",8)
            self.c.drawString(380, y, str(i[1]))
            
            y-=50
            self.c.rect(20, y, 550, 5, fill=True, stroke=False)
            y-=50

        self.c.showPage()
        self.c.save()
        self.printRelatorio()



    def geraRelatFornecedores(self):
        self.c = canvas.Canvas("relatorio.pdf")

         
        result= self.interface_banco.getFornecedorMaisVendas()
        print(result)
        self.c.setFont("VeraBd",16)
        self.c.drawString(200, 790, 'Relatório de Fornecedores')
        y=700
        for i in result:
            self.c.setFont("VeraBd",10)
            self.c.drawString(60, y, '°Forn: ')
            self.c.setFont("Vera",8)
            self.c.drawString(120, y, str(i[0]))

            self.c.setFont("VeraBd",10)
            self.c.drawString(320, y, '°Pedidos: ')
            self.c.setFont("Vera",8)
            self.c.drawString(380, y, str(i[1]))
            
            y-=50
            self.c.rect(20, y, 550, 5, fill=True, stroke=False)
            y-=50

        self.c.showPage()
        self.c.save()
        self.printRelatorio()
    
    def getRelatorioComissao(self):
        self.c = canvas.Canvas("relatorio.pdf")

         
        result= self.interface_banco.getAllComissao()
        print(result)
        self.c.setFont("VeraBd",16)
        self.c.drawString(180, 790, 'Relatório de Comissao')
        y=700
        for i in result:
            self.c.setFont("VeraBd",10)
            self.c.drawString(60, y, '°Vendedor: ')
            self.c.setFont("Vera",8)
            self.c.drawString(140, y, str(i[0]))

            self.c.setFont("VeraBd",10)
            self.c.drawString(280, y, 'Comissao devida: ')
            self.c.setFont("Vera",8)
            self.c.drawString(390, y, str(i[1]))
            
            y-=50
            self.c.rect(20, y, 550, 5, fill=True, stroke=False)
            y-=50
            if y<=150:
                self.c.showPage()
                y=700


        self.c.showPage()
        self.c.save()
        self.printRelatorio()


        

        
    
class Funcs():
    def limpar_tela(self):
        self.codigo_entry.delete(0, END)
        self.vtotal_entry.delete(0, END)
        self.comissao_entry.delete(0, END)
        self.vendedor_cbox.delete(0, END)
        self.produto_cbox.delete(0, END)

    def variaveis(self):
        self.codigo=self.codigo_entry.get()
        self.vtotal=self.vtotal_entry.get()
        self.comissao=self.comissao_entry.get()
        # self.vendedor=self.vendedor.get()
        # self.produto=self.produto.get()


    def gerarVendasUnicas(self):
         
        try:
            self.interface_banco.getIds()
            self.interface_banco.insertNVendas(int(self.codigo_entry.get()))
        except Exception as e:
            print("Número inválido ", end='')
            print(e)
        finally:
            self.limpar_tela()

    def onDoubleClick(self, event):
        self.limpar_tela()
        self.listaVen.selection()

        for n in self.listaVen.selection():
            col1, col2, col3, col4, col5 = self.listaVen.item(n, 'value')
            self.codigo_entry.insert(END, col1)
            self.vtotal_entry.insert(END, col4)
            self.comissao_entry.insert(END, col5)
            self.vendedor_cbox.insert(END, col3)
            self.produto_cbox.insert(END, col2)
              
    
    def check_input_produto(self, event):
        value = event.widget.get()
        if value == '':
            self.produto_cbox['values'] = pList
        else:
            data = []
            for item in pList:
                if value.lower() in item.lower():
                    data.append(item)
            self.produto_cbox['values'] = data

    def check_input_vendedor(self, event):
        value = event.widget.get()
        if value == '':
            self.vendedor_cbox['values'] = vList
        else:
            data = []
            for item in vList:
                if value.lower() in item.lower():
                    data.append(item)
            self.vendedor_cbox['values'] = data

    def insertVenda(self):
        try:
             
            self.variaveis()
            id_vendedor = self.interface_banco.getBy("vendedor","nome",self.vendedor_cbox.get())[0][0]
            id_produto = self.interface_banco.getBy("produto","descricao",self.produto_cbox.get())[0][0]
            self.interface_banco.insertInto("venda",id_produto, id_vendedor,self.vtotal, self.comissao)

        except Exception as e:
            print(str(e))
        finally:
            print("")
            try:
                self.limpar_tela()
                self.getAllVendas()
            except Exception as e:
                print(str(e))


# ########################################################
# ########################################################
#               Alimenta a lista com uma query composta


    def getAllVendas(self):
        try:
             
            self.getAllVendedorName()
            self.getAllProdutoName()
            lista = self.interface_banco.getComposedVenda()
            self.listaVen.delete(*self.listaVen.get_children())
            print(lista)
            for venda in lista:
                self.listaVen.insert("", END, values=venda)
        except Exception as e:
            print(str(e))


# ########################################################
# ########################################################
#                  Alimenta os comboboxs <>
#    
    def getAllVendedorName(self):
        try:
             
            lista = self.interface_banco.getAllFrom("vendedor")
            for i in lista:
                vList.append(i[1])
            self.vendedor_cbox['values']=vList
        except Exception as e:
            print(str(e))

    def getAllProdutoName(self):
        try:
             
            lista = self.interface_banco.getAllFrom("produto")
            for i in lista:
                pList.append(i[2])
            self.produto_cbox['values']=pList
        except Exception as e:
            print(str(e))

# ########################################################
# ########################################################
#               Alimenta os combobox</>     

    def deleteVenda(self):
        self.variaveis()
         
        self.interface_banco.deleteBy("venda",self.codigo)
        self.limpar_tela()
        self.getAllVendas()

    def alteraVenda(self):
        self.variaveis()
         
        id_vendedor = self.interface_banco.getBy("vendedor","nome",self.vendedor_cbox.get())[0][0]
        id_produto = self.interface_banco.getBy("produto","descricao",self.produto_cbox.get())[0][0]

        self.interface_banco.updateBy("venda",self.codigo, id_produto, id_vendedor, self.vtotal, self.comissao )
        self.limpar_tela()
        self.getAllVendas()

    def buscaVendedor(self):
         
        self.listaVen.delete(*self.listaVen.get_children())
        nome = self.nome_entry.get()+"%"
        buscaVendedor = self.interface_banco.getBy("vendedor","nome",nome) 
        for i in buscaVendedor:
            self.listaVen.insert("", END, values=i)
        



class Application(Funcs, Relatorios):
       
        
    def __init__(self):
        self.root=root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.Menus()
        self.interface_banco = interface_db("soulcode","senhasql","54.233.220.253","LOJA")
        root.mainloop()

    def tela(self):
        self.root.title("Gerenciamento")
        self.root.configure(background="#1e3743")
        self.root.geometry("700x500")
        self.root.resizable(True, True) 
        self.root.maxsize(width=900, height= 700)
        self.root.minsize(width=500, height= 400)

    def frames_da_tela(self):
        self.frame_1= Frame(self.root, bd=4, bg="#dfe3ee")
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2= Frame(self.root, bd=4, bg="#dfe3ee")
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2, command= self.limpar_tela)
        self.bt_limpar.place(relx=0.20, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_buscar = Button(self.frame_1, text="Carregar", bd=2, command=self.getAllVendas)#buscaVendedor
        self.bt_buscar.place(relx=0.30, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_criar = Button(self.frame_1, text="Novo", bd=2, command= self.insertVenda)
        self.bt_criar.place(relx=0.60, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2, command= self.alteraVenda)
        self.bt_alterar.place(relx=0.70, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_apagar = Button(self.frame_1, text="Apagar", bd=2, command = self.deleteVenda)
        self.bt_apagar.place(relx=0.80, rely=0.1, relwidth=0.1, relheight=0.15)
        ## Criacao de label e entrada de codigo
        ## ------------------------------------
        self.lb_codigo = Label(self.frame_1, text="Codigo", bg="#dfe3ee")
        self.lb_codigo.place(relx=0.05, rely=0.05)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely = 0.15, relwidth=0.08)

        
        ## Criacao de label e Combobox de Produto
        ## ------------------------------------
        self.lb_produto = Label(self.frame_1, text="Produto", bg="#dfe3ee")
        self.lb_produto.place(relx=0.20, rely=0.30)
        self.produto_cbox = ttk.Combobox(self.frame_1)
        self.produto_cbox.place(relx=0.05, rely = 0.40, relwidth=0.40)
        self.produto_cbox['values'] = vList
        ## Criacao de label e Combobox de Vendedor
        ## ------------------------------------
        self.lb_vendedor = Label(self.frame_1, text="Vendedor", bg="#dfe3ee")
        self.lb_vendedor.place(relx=0.70, rely=0.30)
        self.vendedor_cbox = ttk.Combobox(self.frame_1)
        self.vendedor_cbox.place(relx=0.55, rely = 0.40, relwidth=0.40)
        self.vendedor_cbox['values'] = vList



        ## Criacao de label e entrada de Valor total
        ## ------------------------------------
        self.lb_vtotal = Label(self.frame_1, text="Valor total", bg="#dfe3ee")
        self.lb_vtotal.place(relx=0.20, rely=0.55)
        self.vtotal_entry = Entry(self.frame_1)
        self.vtotal_entry.place(relx=0.15, rely = 0.65, relwidth=0.20)

        ## Criacao de label e entrada de telefone
        ## ------------------------------------
        self.lb_comissao = Label(self.frame_1, text="Comissao", bg="#dfe3ee")
        self.lb_comissao.place(relx=0.70, rely=0.55)
        self.comissao_entry = Entry(self.frame_1)
        self.comissao_entry.place(relx=0.65, rely = 0.65, relwidth=0.20)

    def lista_frame2(self):
        self.listaVen = ttk.Treeview(self.frame_2, height=3, column=("col1","col2","col3","col4","col5"))
        self.listaVen.heading("#0", text="")
        self.listaVen.heading("#1", text="id")
        self.listaVen.heading("#2", text="produto")
        self.listaVen.heading("#3", text="vendedor")
        self.listaVen.heading("#4", text="Valor Total")
        self.listaVen.heading("#5", text="Comissao")  
        
        self.listaVen.column("#0", width=1)
        self.listaVen.column("#1", width=20)
        self.listaVen.column("#2", width=175)
        self.listaVen.column("#3", width=95)
        self.listaVen.column("#4", width=100)
        self.listaVen.column("#5", width=109)

        
        self.listaVen.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaVen.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.86)
        
        self.listaVen.bind("<Double-1>", self.onDoubleClick)
        self.produto_cbox.bind('<KeyRelease>', self.check_input_produto)
        self.vendedor_cbox.bind('<KeyRelease>', self.check_input_vendedor)


    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu= Menu(menubar, tearoff=0)
        filemenu2= Menu(menubar, tearoff=0)
        filemenu3= Menu(menubar, tearoff=0)

        def Quit(): self.root.destroy()
        menubar.add_cascade(label="Opções",activebackground="#ff9966", menu=filemenu)
        menubar.add_cascade(label="Relatorios",activebackground="#ff9966", menu=filemenu2)
        menubar.add_cascade(label="Automação",activebackground="#ff9966", menu=filemenu3)

        filemenu.add_command(label="Sair",activebackground="#ff9966", command = Quit)
        filemenu2.add_command(label="Balanço de venda",activebackground="#ff9966", command = self.geraRelatBalanco)
        filemenu2.add_command(label="Ranking venda(valor)",activebackground="#ff9966", command = self.geraRelatMaiorVenda)
        filemenu2.add_command(label="Ranking venda(quantidade)",activebackground="#ff9966", command = self.geraRelatMaiorQuant)
        filemenu2.add_command(label="Ranking fornecedores",activebackground="#ff9966", command = self.geraRelatFornecedores)
        filemenu2.add_command(label="Comissão devida",activebackground="#ff9966", command = self.getRelatorioComissao)

        filemenu3.add_command(label="Gerar vendas unicas",activebackground="#ff9966", command = self.gerarVendasUnicas)
Application()