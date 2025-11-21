# RESUMO — Padrões de Projeto Aplicados ao Sistema de Pedidos

Este documento apresenta um resumo teórico e prático sobre os padrões de projeto utilizados no sistema de pedidos desenvolvido como parte da disciplina da PUC Campinas.

O objetivo é demonstrar domínio conceitual e aplicado de cada padrão, deixando claro **por que** foi escolhido, **qual dor de design resolve** e **como aparece no código**.

---

## 1. Introdução

Em sistemas em crescimento, o código tende a sofrer de problemas como:

- acoplamento excessivo,
- dificuldade para incluir novas funcionalidades,
- dependência rígida de serviços externos,
- lógica duplicada ou espalhada,
- baixa extensibilidade.

Para evitar isso, padrões de projeto auxiliam a estruturar o sistema de forma limpa, modular e escalável.

O sistema apresentado implementa quatro padrões clássicos:

- **Strategy**
- **Adapter**
- **Observer**
- **Factory Method**

---

## 2. Padrões Utilizados

### 2.1. Strategy

**Categoria:** Comportamental  
**Problema que resolve:**  
Sem Strategy, a classe `Order` ficaria cheia de condicionais (`if/else`) para calcular o total com diferentes regras, dificultando manutenção.

**Solução:**  
Encapsular comportamentos em classes separadas e intercambiáveis.

**No código:**

- Interface `PricingStrategy`
- Estratégias concretas:
  - `DefaultPricingStrategy`
  - `DiscountPricingStrategy`
- A classe `Order` aceita qualquer estratégia via `set_pricing_strategy`.

**Benefício:**  
Extensibilidade: novas regras de cálculo podem ser criadas sem alterar o núcleo do sistema.

---

### 2.2. Adapter

**Categoria:** Estrutural  
**Problema que resolve:**  
O sistema precisava usar um serviço legado de frete (`LegacyShippingService`) com interface incompatível.

**Solução:**  
Criar um adaptador (`ShippingAdapter`) que converte chamadas entre o sistema atual e o legado.

**No código:**

- Classe `LegacyShippingService`
- Classe `ShippingAdapter`

**Benefício:**  
Desacoplamento da API antiga, permitindo trocar o serviço futuramente sem alterar a lógica principal.

---

### 2.3. Observer

**Categoria:** Comportamental  
**Problema que resolve:**  
O sistema precisava disparar ações (prints, notificações, logs) automaticamente após eventos, sem acoplar essas ações dentro da classe `Order`.

**Solução:**  
Implementar um mecanismo onde observadores são registrados e notificados sempre que o pedido muda de estado.

**No código:**

- Interface `OrderObserver`
- Observadores concretos:
  - `PrintObserver`
  - `EmailObserver` (simulado)
- Método `notify_observers` dentro de `Order`.

**Benefício:**  
Permite adicionar ou remover notificações sem tocar no código principal.

---

### 2.4. Factory Method

**Categoria:** Criacional  
**Problema que resolve:**  
Sem Factory Method, o sistema dependeria diretamente de classes concretas de pagamento (`PixPaymentProcessor`, `CreditCardPaymentProcessor`). Isso geraria acoplamento e exigiria modificar o código sempre que um novo método fosse adicionado.

**Solução:**  
Criar uma fábrica (`PaymentProcessorFactory`) que retorna o processador correto com base no tipo de pagamento.

**No código:**

- `PaymentProcessorFactory.create_processor(tipo)`
- Processadores concretos:
  - `PixPaymentProcessor`
  - `CreditCardPaymentProcessor`

**Benefício:**  
Facilidade para adicionar novos processadores sem alterar o fluxo do sistema.

---

## 3. Conclusão

Os padrões implementados garantem:

- **organização modular**,
- **baixa dependência entre componentes**,
- **facilidade de evolução**,
- **código limpo e legível**,
- **aplicação correta de boas práticas de engenharia**.

O sistema demonstra domínio técnico e conceitual dos padrões Strategy, Adapter, Observer e Factory Method em um cenário realista.

---

## 4. Autores

Gabriel Ferraro Ferragute - 23013742
Rafael Oliveira Silva - 23002269
