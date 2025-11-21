# Sistema de Pedidos com Padrões de Projeto (Python)

Este projeto implementa um sistema simples de pedidos utilizando os seguintes padrões de projeto:

- **Strategy**
- **Adapter**
- **Observer**
- **Factory Method**

Além disso, o projeto segue uma estrutura modular clara, separando domínio, padrões e camada de execução.

---

## 1. Objetivo

Demonstrar domínio prático de padrões de projeto aplicados a um sistema realista de pedidos, garantindo:

- Baixo acoplamento entre componentes
- Facilidade de manutenção e evolução
- Extensibilidade para novos comportamentos
- Integração com serviço legado de forma controlada

---

## 1.1. Dor de Design (antes dos padrões)

Sem os padrões de projeto, este sistema apresentaria várias dores de arquitetura:

### **Dores identificadas**

- A classe `Order` precisaria fazer **tudo**: calcular preço, aplicar regras, chamar serviço de frete, enviar notificações, processar pagamento.
- A lógica de cálculo de preços ficaria cheia de `if/else`, dificultando alterar ou adicionar novos tipos de desconto.
- A integração com o serviço de frete legado obrigaria a aplicação a depender diretamente da API antiga e instável.
- Para cada novo meio de pagamento, seria necessário modificar o fluxo principal, aumentando o acoplamento.
- Notificações (print, email, logs) ficariam espalhadas dentro da classe `Order`, misturando responsabilidades e prejudicando manutenção.

### **Como os padrões resolvem isso**

- **Strategy** → Remove `if/else` de cálculo de preço e permite trocar regras dinamicamente.
- **Adapter** → Cria uma camada intermediária limpa para integrar o serviço legado.
- **Factory Method** → Evita `new` espalhado pela aplicação e facilita adicionar novos meios de pagamento.
- **Observer** → Desacopla notificações do fluxo principal do pedido.

---

## 2. Estrutura do Projeto

```
.
├── main.py
├── domain
│   ├── order.py
│   ├── models.py
│   └── __init__.py
├── patterns
│   ├── strategy.py
│   ├── adapter.py
│   ├── observer.py
│   ├── factory_method.py
│   └── __init__.py
├── README.md
└── RESUMO.md
```

### **Descrição**

- `domain/` → classes de negócio (`Order`, `Product`, `OrderItem`)
- `patterns/` → implementação dos padrões
- `main.py` → ponto central do sistema, demonstrando o uso dos padrões

---

## 3. Padrões Implementados e Localização no Código

### **1. Strategy – strategy.py**

Usado para cálculo de total do pedido.

- Problema: múltiplas regras de preço gerariam muito `if`.
- Solução: encapsular regras em estratégias trocáveis.
- Classes envolvidas:
  - `PricingStrategy`
  - `DefaultPricingStrategy`
  - `DiscountPricingStrategy`
- Onde é usado:
  - `Order.set_pricing_strategy()`

---

### **2. Adapter – adapter.py**

Usado para integrar com serviço legado de frete.

- Problema: API de frete antiga e incompatível com o novo sistema.
- Solução: criar um adaptador que converte chamadas.
- Classes envolvidas:
  - `LegacyShippingService`
  - `ShippingAdapter`
- Onde é usado:
  - Dentro de `Order.calculate_shipping()`

---

### **3. Observer – observer.py**

Usado para notificar eventos automaticamente.

- Problema: notificações acopladas ao fluxo de pedido.
- Solução: permitir múltiplos observadores independentes.
- Classes:
  - `OrderObserver`
  - `PrintObserver`
  - `EmailObserver` (simulação)
- Onde é usado:
  - `Order.notify_observers()`

---

### **4. Factory Method – factory_method.py**

Usado para criar processadores de pagamento.

- Problema: criação manual e acoplada de classes concretas.
- Solução: encapsular criação em fábrica.
- Classes:
  - `PaymentProcessorFactory`
  - `PixPaymentProcessor`, `CreditCardPaymentProcessor`
- Onde é usado:
  - `Order.process_payment()`

---

## 4. Fluxo do Sistema

1. Criar produtos e pedido
2. Definir estratégia de preço
3. Integrar serviço de frete via Adapter
4. Registrar observers
5. Processar pagamento via Factory Method
6. Observar notificações automáticas

Todo o fluxo está demonstrado em `main.py`.

---

## 5. Como Executar

### Pré-requisitos

- Python 3.10+
- Nenhuma dependência externa

### Comando

```bash
python main.py
```

---

## 6. Conclusão

Este projeto demonstra domínio claro e aplicado dos padrões:

- Strategy
- Adapter
- Observer
- Factory Method

Cada padrão resolve uma dor de design real e melhora a arquitetura do sistema de forma modular e extensível.

---

## 7. Autor

Gabriel Ferraro Ferragute - 23013742
Rafael Oliveira Silva - 23002269
