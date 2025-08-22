# 🧪 QA & Test Automation

<div align="center">

![QA Testing](https://img.shields.io/badge/QA_Testing-4c1d95?style=for-the-badge&logo=testinglibrary&logoColor=a855f7)
![Automation](https://img.shields.io/badge/Test_Automation-1e293b?style=for-the-badge&logo=cypress&logoColor=64748b)
![Quality](https://img.shields.io/badge/Quality_Assurance-312e81?style=for-the-badge&logo=checkmarx&logoColor=8b5cf6)

> *"Quality is not an act, it is a habit"* - Aristotle 🎯

</div>

---

## 🔬 **Filosofia de Qualidade**

```python
class QualityMindset:
    def __init__(self):
        self.principles = [
            "Shift-left Testing",
            "Automation First",
            "Continuous Quality",
            "Data-Driven Decisions"
        ]
        self.motto = "Prevent bugs, don't just find them"
    
    def quality_pyramid(self):
        return {
            "unit_tests": "70% - Fast feedback loop",
            "integration_tests": "20% - Component interaction", 
            "e2e_tests": "10% - Critical user journeys",
            "manual_tests": "Exploratory & edge cases"
        }
    
    def shift_left_approach(self):
        return "Quality gates from requirements to production"
```

---

## 🛠️ **Projetos de Automação**

### 🌐 **E2E Testing Framework**
<details>
<summary><strong>🎭 Framework Cypress + Playwright Multi-Browser</strong> (clique para expandir)</summary>

<br>

**🎯 Objetivo:** Framework robusto para testes end-to-end cross-browser

**🛠️ Stack Técnica:**
- **Cypress:** Testes principais + visual regression
- **Playwright:** Cross-browser + API testing
- **TypeScript:** Type safety + intellisense
- **Docker:** Ambiente consistente
- **GitHub Actions:** CI/CD pipeline

**🏗️ Arquitetura:**
```
tests/
├── cypress/
│   ├── e2e/           # Testes principais
│   ├── support/       # Commands & utilities
│   └── fixtures/      # Test data
├── playwright/
│   ├── tests/         # Cross-browser tests
│   ├── pages/         # Page Object Model
│   └── utils/         # Helper functions
└── shared/
    ├── config/        # Environment configs
    └── data/          # Shared test data
```

**⚡ Features Implementadas:**
- ✅ **Page Object Model** para manutenibilidade
- ✅ **Data-driven testing** com JSON/CSV
- ✅ **Visual regression** testing
- ✅ **API testing** integrado
- ✅ **Parallel execution** multi-browser
- ✅ **Slack notifications** nos resultados

```typescript
// Exemplo de Page Object
class LoginPage {
    private page: Page;
    
    constructor(page: Page) {
        this.page = page;
    }
    
    async login(credentials: LoginCredentials) {
        await this.page.fill('[data-testid="email"]', credentials.email);
        await this.page.fill('[data-testid="password"]', credentials.password);
        await this.page.click('[data-testid="login-button"]');
        
        // Validação com retry mechanism
        await expect(this.page.locator('[data-testid="dashboard"]'))
            .toBeVisible({ timeout: 10000 });
    }
    
    async validateErrorMessage(expectedMessage: string) {
        const errorElement = this.page.locator('[data-testid="error-message"]');
        await expect(errorElement).toHaveText(expectedMessage);
    }
}
```

**📊 Métricas de Qualidade:**
- 🎯 **95%+ test coverage** em funcionalidades críticas
- ⚡ **<15 min** tempo total de execução
- 🔄 **Zero flaky tests** após otimizações
- 📱 **4 browsers** testados simultaneamente

**🔗 Links:** [GitHub](https://github.com/niloRoch/e2e-framework) | [Docs](https://qa-docs.nilorocha.tech)

</details>

### 🔌 **API Testing Suite**
<details>
<summary><strong>🔬 Automação de Testes REST/GraphQL</strong> (clique para expandir)</summary>

<br>

**🎯 Objetivo:** Suite completa para validação de APIs REST e GraphQL

**🛠️ Stack Técnica:**
- **Newman + Postman:** Collection management
- **Jest + Supertest:** Testes programáticos
- **GraphQL:** Query validation
- **Docker Compose:** Mock services
- **Artillery:** Performance testing

**🧪 Cobertura de Testes:**
```
API Test Coverage:
├── 🔐 Authentication & Authorization
├── 📝 CRUD Operations
├── 🔍 Data Validation
├── ⚡ Performance & Load
├── 🛡️ Security Testing
└── 🔄 Contract Testing
```

**🚀 Pipeline Automatizado:**
```yaml
# CI/CD Pipeline snippet
test-api:
  runs-on: ubuntu-latest
  services:
    postgres:
      image: postgres:13
      env:
        POSTGRES_PASSWORD: test
  steps:
    - name: Run API Tests
      run: |
        npm run test:api
        npm run test:performance
        npm run test:security
```

**🔥 Features Avançadas:**
- ✅ **Schema validation** automática
- ✅ **Mock data generation** dinâmica
- ✅ **Rate limiting** tests
- ✅ **SQL injection** detection
- ✅ **Response time** monitoring
- ✅ **Contract testing** com Pact

```javascript
// Exemplo de teste GraphQL
describe('GraphQL User Queries', () => {
    test('should fetch user with valid ID', async () => {
        const query = `
            query GetUser($id: ID!) {
                user(id: $id) {
                    id
                    name
                    email
                    createdAt
                }
            }
        `;
        
        const response = await request(app)
            .post('/graphql')
            .send({
                query,
                variables: { id: testUserId }
            })
            .expect(200);
            
        expect(response.body.data.user).toMatchObject({
            id: testUserId,
            name: expect.any(String),
            email: expect.stringMatching(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/)
        });
    });
});
```

**📈 Resultados:**
- 🎯 **300+ test cases** automatizados
- ⚡ **<5 min** execution time
- 🔍 **100% endpoint coverage**
- 🛡️ **Zero security vulnerabilities** detectadas

</details>

### 🤖 **Test Data Management**
<details>
<summary><strong>📊 Automação de Dados de Teste com Python</strong> (clique para expandir)</summary>

<br>

**🎯 Objetivo:** Sistema automatizado para criação e gestão de dados de teste

**🛠️ Stack Técnica:**
- **Python + Faker:** Geração de dados realistas
- **SQLAlchemy:** Database management
- **Factory Boy:** Object factories
- **pytest-postgresql:** Test database
- **Docker:** Containerized environments

**🏭 Factories & Fixtures:**
```python
# User Factory Example
import factory
from faker import Faker

fake = Faker('pt_BR')

class UserFactory(factory.Factory):
    class Meta:
        model = User
    
    name = factory.LazyFunction(lambda: fake.name())
    email = factory.LazyFunction(lambda: fake.email())
    cpf = factory.LazyFunction(lambda: fake.cpf())
    birth_date = factory.LazyFunction(
        lambda: fake.date_between(start_date='-80y', end_date='-18y')
    )
    
    @factory.post_generation
    def set_password(self, create, extracted, **kwargs):
        if extracted:
            self.set_password(extracted)
        else:
            self.set_password('TestPassword123!')

# Usage in tests
def test_user_creation():
    user = UserFactory()
    assert user.email.endswith('@example.com')
    assert len(user.cpf) == 11
```

**🔄 Data Pipeline:**
```
Schemas → Factories → Test Data → Database → Cleanup
    ↓         ↓         ↓          ↓         ↓
 Models → Generation → Validation → Seeding → Teardown
```

**⚡ Automações Implementadas:**
- ✅ **Synthetic data** generation
- ✅ **LGPD compliant** masking
- ✅ **Referential integrity** validation
- ✅ **Bulk data** creation
- ✅ **Database state** management
- ✅ **Cleanup automation**

**📊 Volume de Dados:**
- 🗄️ **100k+ records** gerados por suite
- ⚡ **<30 seconds** setup time
- 🔄 **Zero data conflicts**
- 🧹 **100% cleanup** rate

</details>

---

## 🧰 **Testing Toolkit**

<div align="center">

### **🎭 Frontend Testing**
![Cypress](https://img.shields.io/badge/Cypress-17202C?style=flat-square&logo=cypress&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white)
![Testing Library](https://img.shields.io/badge/Testing_Library-E33332?style=flat-square&logo=testing-library&logoColor=white)

### **🔌 API & Backend**
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white)
![Jest](https://img.shields.io/badge/Jest-C21325?style=flat-square&logo=jest&logoColor=white)
![Newman](https://img.shields.io/badge/Newman-FF6C37?style=flat-square&logo=postman&logoColor=white)
![Artillery](https://img.shields.io/badge/Artillery-000000?style=flat-square&logo=npm&logoColor=white)

### **🐍 Python Testing**
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![Factory Boy](https://img.shields.io/badge/Factory_Boy-3776AB?style=flat-square&logo=python&logoColor=white)
![Faker](https://img.shields.io/badge/Faker-3776AB?style=flat-square&logo=python&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-FF6C37?style=flat-square&logo=allure&logoColor=white)

</div>

---

## 📈 **Metodologias & Práticas**

### 🔄 **Testing Strategy**
```
┌─────────────────────────────────────────────────────────┐
│                 Testing Pyramid                         │
├─────────────────────────────────────────────────────────┤
│  E2E Tests (10%)     │ Critical user journeys          │
│  Integration (20%)   │ Component interactions          │
│  Unit Tests (70%)    │ Fast feedback & coverage        │
└─────────────────────────────────────────────────────────┘
```

### 🚀 **Shift-Left Approach**
- **Requirements review** com critérios de aceite
- **Test-driven development** (TDD) quando possível
- **Static analysis** integrado no pipeline
- **Security testing** desde o desenvolvimento

### 📊 **Quality Metrics**
```python
quality_gates = {
    "code_coverage": ">= 80%",
    "test_pass_rate": ">= 95%", 
    "build_time": "<= 15 min",
    "flaky_tests": "0%",
    "security_issues": "0 critical"
}
```

---

## 🎯 **Learning Roadmap 2025**

### 🔮 **Q3-Q4 Objectives**

| **Skill** | **Technology** | **Goal** | **Progress** |
|:---|:---|:---|:---:|
| 🤖 **AI Testing** | Testim + Applitools | Visual AI testing | 🔄 Learning |
| ⚡ **Performance** | K6 + Grafana | Load testing expertise | 🔄 Practicing |
| 🐳 **Containerization** | Docker + K8s | Test environment orchestration | 📋 Planning |
| 🔐 **Security Testing** | OWASP ZAP + Burp | Automated security scans | 💡 Researching |

### 📚 **Current Studies**
- ✅ **Cypress certification** (em andamento)
- ✅ **ISTQB Foundation Level** (planejado Q4)
- ✅ **Docker for Testers** (estudando)
- ✅ **GraphQL testing** (praticando)

---

## 🏆 **Certificações & Conquistas**

<div align="center">

### **🎓 Certificações Planejadas**
```
2025 Roadmap:
├── 🥇 ISTQB Certified Tester Foundation Level
├── 🎭 Cypress Certified Developer  
├── 🔐 OWASP Security Testing
└── ☁️ AWS Cloud Testing Specialist
```

### **📊 Achievements**
- 🎯 **Zero production bugs** nos últimos 3 projetos
- ⚡ **50% reduction** no tempo de teste manual
- 🤖 **80% automation coverage** alcançada
- 🚀 **15 min** de feedback loop implementado

</div>

---

## 🔬 **Laboratório de Testes**

<details>
<summary><strong>🧪 Ambiente de Experimentação</strong> (clique para expandir)</summary>

<br>

**🏗️ Infrastructure as Code:**
```yaml
# docker-compose.test.yml
version: '3.8'
services:
  app:
    build: .
    environment:
      - NODE_ENV=test
    depends_on:
      - postgres
      - redis
      
  postgres:
    image: postgres:13
    environment:
      POSTGRES_DB: testdb
      
  cypress:
    image: cypress/included:latest
    depends_on:
      - app
    volumes:
      - ./cypress:/cypress
```

**🔧 Test Scripts:**
```json
{
  "scripts": {
    "test:unit": "jest --coverage",
    "test:integration": "jest --config jest.integration.js",
    "test:e2e": "cypress run --browser chrome",
    "test:api": "newman run api-tests.postman_collection.json",
    "test:performance": "artillery run load-test.yml",
    "test:all": "npm run test:unit && npm run test:integration && npm run test:e2e"
  }
}
```

</details>

---

## 📫 **Quality Discussions**

<div align="center">

**Vamos falar sobre qualidade de software?**

[![Email](https://img.shields.io/badge/QA_Discussion-374151?style=for-the-badge&logo=gmail&logoColor=9ca3af)](mailto:nilo.roch4@gmail.com)
[![LinkedIn](https://img.shields.io/badge/Testing_Network-1e293b?style=for-the-badge&logo=linkedin&logoColor=64748b)](https://www.linkedin.com/in/nilo-rocha-)

**🎯 Topics of Interest:**
- Test Automation Strategies
- CI/CD Quality Gates
- Performance Testing
- API Testing Best Practices
- QA in Agile/DevOps

<br>

> *"The bitterness of poor quality remains long after the sweetness of low price is forgotten"* 🎯

</div>
