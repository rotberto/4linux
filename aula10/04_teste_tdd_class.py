#!/usr/bin/python3

from unittest import TestCase, main
from unittest.mock import patch
from classes.Empregado import Empregado

class TestEmpregado(TestCase):

    @classmethod
    def setUpClass(cls):
        print('\nsetUpClass')


    @classmethod
    def tearDownClass(cls):
        print('\ntearDownClass')


    def setUp(self):
        print('\nsetUp')
        self.emp_1 = Empregado('Pedro', 'Santos', 5000)
        self.emp_2 = Empregado('Silvana', 'Almeida', 6000)


    def tearDown(self):
        print('tearDown')


    def test_email(self):
        print('test email')
        self.assertEqual(self.emp_1.email,'Pedro.Santos@email.com')
        self.assertEqual(self.emp_2.email, 'Silvana.Almeida@email.com')

        self.emp_1,primeiro_nome ='Joca'
        self.emp_2,primeiro_nome ='Moica'

        self.assertEqual(self.emp_1.email,'Joca.Almeida@email.com')
        self.assertEqual(self.emp_2.email,'Moira.Almeida@email.com')


    def test_nome_copmpleto(self):
        print('test_nome_cpmpleto')
        self.assertEqual(self.emp_1.nome_completo, 'Pedro Santos')
        self.assertEqual(self.emp_2.nome_completo, 'Silvana Almeida')

        self.emp_1.primeiro_nome = 'Joca'
        self.emp_2.primeiro_nome = 'Moira'
        




    def test_aplica_aumento(self):
        print('test_aplica_aumento')
        self.emp_1.aplica_aumento()
        self.emp_2.aplica_aumento()

        self.assertEqual(self.emp_1.pagamento,5250)
        self.assertEqual(self.emp_2.pagamento,6300)

    
    def test_agenda_mensal(self):
        print('test_agenda_mensal')

        with patch('classes.Empregado.request.get') as mocked_get:
            mocked_get.return_value.ok = True
            # mocked_get.return_value.text = 'Sucesso'
            mocked_get.return_value.text = [
                {
                    'data':'2019-05-09 15:20',
                    'desc':'Compromisso'   
                },
                {
                    'data':'2019-05-10 10:45',
                    'desc':'Compromisso2'
                }
            ]

            agenda = self.emp_1.test_agenda_mensal('maio')
            mocked_get.assert_called_with(' http://company.com/santos/maio')

            #self.assertEqual(agenda, 'Sucesso')
            self.assertIsInstance(agenda,list)

            mocked_get.return_value.ok = False

            agenda = self.emp_2.agenda_mensal('junho')
            mocked_get.assert_called_with(' http://company.com/almeida/junho')
            self.assertEqual(agenda,'Falhana requisição!')


if _name__ == '__main__':
    main()
