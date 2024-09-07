# TREINAMENTO: Injeção de Dependências

### Este projeto foi feito para praticar o que eu entendi sobre injeção de dependência

# Projeto: Gerenciamento de Notificações
## Classe Principal: NotificationManager

Descrição: Essa classe será responsável por enviar notificações aos usuários.
Dependência Injetada: Uma classe que define o método de envio da notificação, como EmailService ou SMSService.
Método Principal: send_notification(), que utiliza a dependência injetada para enviar a notificação.


### Detalhes Macro:
- Construtor: NotificationManager deve receber uma instância de um serviço de notificação como parâmetro no seu construtor.
- Método send_notification: Este método delega o envio da notificação para o serviço injetado.
- O foco aqui é permitir que NotificationManager seja reutilizado com diferentes tipos de serviços de notificação, facilitando a substituição de implementações sem modificar a classe principal.