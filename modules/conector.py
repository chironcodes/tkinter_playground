import mysql.connector

import random




class interface_db:

    fornecedor = "INSERT INTO fornecedor (nome, cnpj) VALUES('{}', '{}');"
    produto = "INSERT INTO produto (id_fornecedor, descricao, preco, qtd_estoque) VALUES ({}, '{}', '{}', {});"
    venda = "INSERT INTO venda(id_produto, id_vendedor, valor_total, comissao) VALUES ({}, {}, '{}', '{}');"
    vendedor = "INSERT INTO vendedor (nome, cpf, endereco, telefone) VALUES('{}', '{}', '{}', '{}');"


    upFornecedor = "UPDATE fornecedor SET nome='{}', CNPJ='{}' WHERE id_fornecedor={};"
    upProduto = "UPDATE produto SET id_fornecedor={}, descricao='{}', preco='{}', qtd_estoque={} WHERE id_produto={};"
    upVenda = "UPDATE venda SET id_produto={}, id_vendedor={}, valor_total='{}', comissao='{}' WHERE id_venda={};"
    upVendedor = "UPDATE vendedor SET nome='{}', cpf='{}', endereco='{}', telefone='{}' WHERE id_vendedor={};"
    
    def __init__(self, user, password, host, database):
        try:
            self.user=user
            self.password =password
            self.host = host
            self.database = database
        except Exception as e:
            print(str(e))

    def conectar(self):
        try:
            con = mysql.connector.connect(user = self.user, password = self.password, host = self.host, database = self.database)
            cursor = con.cursor()
            return con, cursor
        except Exception as e:
            print(str(e))


    def desconectar(self, con, cursor):
        try:
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print(str(e))


    def getAllFrom(self, table:str):
        try:
            con,cursor = self.conectar()
            query = "Select * from {};".format(table)
            cursor.execute(query)
            return cursor.fetchall() 
        except Exception as e:
            print(str(e))

    def getBy(self, table:str, param:str, value):
        print(type(value))
        try:
            con,cursor = self.conectar()
            if isinstance(value,int):
                query = "SELECT * FROM {} WHERE {} LIKE {};".format(table, param, value)
            else:
                query = "SELECT * FROM {} WHERE {} LIKE '{}';".format(table, param, value)
            print(query)
            cursor.execute(query)
            return cursor.fetchall() 
        except Exception as e:
            print(str(e))

    

    def deleteBy(self, table:str, value:int):
        try:
            con, cursor = self.conectar()
            query = "DELETE FROM {} WHERE id_{}={};".format(table,table,value)
            print(query)
            s =cursor.execute(query)
            self.desconectar(con,cursor)
            print(s[0]);
        except Exception as e:
            print(str(e))

    def updateBy(self, table:str, value:int, *args):
        try:
            con, cursor = self.conectar()
            if table=="fornecedor":
                query = self.upFornecedor.format(args[0],args[1],value)
                print(query)
            elif table=="produto":
                query = self.upProduto.format(int(args[0]),args[1],args[2],int(args[3]),value)
                print(query)
            elif table=="venda":
                query = self.upVenda.format(args[0],args[1],args[2],args[3],value)
                print(query)
            elif table=="vendedor":
                query = self.upVendedor.format(args[0],args[1],args[2],args[3],value)
                print(query)
            else:
                print("Error: Tabela inexistente. Tente novamente")

            cursor.execute(query)
            self.desconectar(con,cursor)
        except Exception as e:
            print(str(e))
            


    def insertInto(self, table:str, *args):
        try:
            con, cursor = self.conectar()
            if table=="fornecedor":
                query = self.fornecedor.format(args[0],args[1])
                print(query)
            elif table=="produto":
                query = self.produto.format(int(args[0]),args[1],args[2],int(args[3]))
                print(query)
            elif table=="venda":
                query = self.venda.format(args[0],args[1],args[2],args[3])
                print(query)
            elif table=="vendedor":
                query = self.vendedor.format(args[0],args[1],args[2],args[3])
                print(query)
            else:
                print("Error: Tabela inexistente. Tente novamente")

            cursor.execute(query)
            self.desconectar(con,cursor)
        except Exception as e:
            print(str(e))











# ########################################################
# ########################################################
#                     FUNCAO DE VENDAS

    def getTotalVendas(self):
        try:
            con,cursor = self.conectar()
            query = "SELECT SUM(valor_total) FROM venda;"
            cursor.execute(query)
            return cursor.fetchall()[0][0] 
        except Exception as e:
            print(str(e))



    def getFuncionarioMaiorValor(self):
        try:
            con,cursor = self.conectar()
            query = "SELECT vendedor.nome, venda.valor_total AS total FROM venda, vendedor  WHERE venda.id_vendedor=vendedor.id_vendedor  ORDER BY total DESC LIMIT 5;"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))

    def getFuncionarioMaisVendas(self):
        try:
            con,cursor = self.conectar()
            query = "SELECT vendedor.nome, COUNT(vendedor.nome) AS qtd_vendas FROM vendedor, venda WHERE vendedor.id_vendedor=venda.id_vendedor GROUP BY vendedor.nome ORDER BY COUNT(*) DESC LIMIT 5;"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        
    def getFornecedorMaisVendas(self):
        try:
            con,cursor = self.conectar()
            query = "SELECT fornecedor.nome, COUNT(venda.valor_total) AS vendas FROM fornecedor, produto, venda WHERE fornecedor.id_fornecedor=produto.id_fornecedor AND produto.id_produto=venda.id_produto GROUP BY fornecedor.nome ORDER BY vendas DESC LIMIT 5;"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))

    def getAllComissao(self):
        try:
            con,cursor = self.conectar()
            query = "SELECT vendedor.nome, (SUM(venda.valor_total)*0.08) as total FROM vendedor, venda WHERE vendedor.id_vendedor=venda.id_vendedor GROUP BY vendedor.nome ORDER BY total DESC;"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))



# ########################################################
# ########################################################
#                   METODOS DE GUI


    def getComposedVenda(self):
        try:
            con,cursor = self.conectar()
            query = "SELECT venda.id_venda, produto.descricao, vendedor.nome, venda.valor_total, venda.comissao FROM  produto, venda, vendedor WHERE  venda.id_vendedor = vendedor.id_vendedor AND venda.id_produto = produto.id_produto;"
            cursor.execute(query)
            return cursor.fetchall() 
        except Exception as e:
            print(str(e))

   








# ########################################################
# ########################################################
#                   GAMBIARRA


    
    idForn=[]
    idProd=[]
    idVend=[]

    def showTables(self):
        try:
            con, cursor = self.conectar()
            query = "SHOW TABLES;"
            cursor.execute(query)
            return cursor.fetchall()            
        except Exception as e:
            print(str(e))


    def getIds(self):
        self.idForn = self.getAllFrom("fornecedor");
        self.idProd =self.getAllFrom("produto");
        self.idVend =self.getAllFrom("vendedor");

        for i in range(len(self.idForn)):
            self.idForn[i]=self.idForn[i][0]
        for i in range(len(self.idProd)):
            self.idProd[i]=self.idProd[i][0]
        for i in range(len(self.idVend)):
            self.idVend[i]=self.idVend[i][0]

            
    def getUniqueIds(self,table:str, qtd:int):
        i=0
        uniqueIds=[]
        if table=="fornecedor":
            while(i<qtd):
                n=random.randint(0,len(self.idForn)-1)
                if self.idForn[n]!=-1:
                    i+=1
                    uniqueIds.append(self.idForn[n])
                    print("Fnumero unico",self.idForn[n])
                    self.idForn[n]=-1 
        elif table=="produto":
            while(i<qtd):
                n=random.randint(0,len(self.idProd)-1)
                if self.idProd[n]!=-1:
                    i+=1
                    uniqueIds.append(self.idProd[n])
                    print("P numero unico",self.idProd[n])
                    self.idProd[n]=-1 
        elif table=="vendedor":
            while(i<qtd):
                n=random.randint(0,len(self.idVend)-1)
                if self.idVend[n]!=-1:
                    i+=1
                    uniqueIds.append(self.idVend[n])
                    print("V numero unico",self.idVend[n])
                    self.idVend[n]=-1 

        return uniqueIds; 



    def insertNVendas(self, num:int):
        
        idP=self.getUniqueIds("produto",num)
        idV=self.getUniqueIds("vendedor",num)
        
        for i in range(num):
            self.insertInto("venda",idP[i],idV[i], round(random.uniform(00.5, 64.5),2),round(random.uniform(0.5, 4.5),2))
        

        
        