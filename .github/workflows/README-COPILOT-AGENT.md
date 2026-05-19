# 🤖 Copilot CLI Agent (Business Plan) - Guia de Uso

## 📋 Visão Geral

Este workflow permite que o **GitHub Copilot Agent** (com plano Business e Claude Sonnet 4.5) edite arquivos do repositório diretamente, similar ao comportamento no VS Code.

## 🔧 Configuração Inicial

### 1. Configure o Secret no GitHub

1. Vá em: **Settings** → **Secrets and variables** → **Actions**
2. Clique em **New repository secret**
3. Configure:
   - **Name**: `COPILOT_BUSINESS_TOKEN`
   - **Value**: Seu token Fine-Grained do GitHub com acesso ao Copilot Business
   
#### ⚠️ IMPORTANTE: Use Fine-Grained Token (NÃO Classic)

**O Copilot CLI NÃO aceita Classic Personal Access Tokens (ghp_)**

Você DEVE usar um **Fine-Grained Token (github_pat_)**

#### Como gerar o Fine-Grained Token correto:

1. **Acesse**: https://github.com/settings/tokens?type=beta

2. **Clique em**: **Generate new token** (na seção Fine-grained tokens)

3. **Configure o token**:
   
   - **Token name**: `Copilot Business Token` (ou qualquer nome descritivo)
   
   - **Expiration**: Escolha a duração (30, 60, 90 dias, ou Custom)
   
   - **Description** (opcional): `Token para GitHub Copilot CLI Business`
   
   - **Repository access**: 
     - Selecione **"All repositories"** OU
     - Selecione **"Only select repositories"** e escolha seu repositório

4. **Permissions**:

   **A) Repository permissions** (permissions de repositório):
   
   Expanda "Repository permissions" e configure:
   
   - ✅ **Contents**: `Read and write` (para criar commits)
   - ✅ **Pull requests**: `Read and write` (para criar PRs)
   - ✅ **Workflows**: `Read and write` (para editar arquivos em .github/workflows/)
   - ✅ **Metadata**: `Read-only` (obrigatório, selecionado automaticamente)
   
   **B) Account permissions** (permissions de conta - OBRIGATÓRIO para Copilot):
   
   ⚠️ **CRÍTICO**: Role para baixo até encontrar **"Account permissions"**
   
   Expanda "Account permissions" e configure:
   
   - ✅ **Copilot Chat**: `Read and write` OU `Read` (OBRIGATÓRIO!)
   
   OU se não aparecer "Copilot Chat", procure por:
   
   - ✅ **Copilot**: `Read` (OBRIGATÓRIO!)
   
   **Nota**: Essas permissões de Copilot estão em **Account permissions** (no final da página), NÃO em Repository permissions!

5. **Clique em**: **Generate token**

6. **⚠️ COPIE O TOKEN AGORA** (você só verá uma vez!)
   - O token começará com: `github_pat_`
   - Exemplo: `github_pat_11AAAAAA...`

7. **Cole no Secret do repositório**:
   - Vá em seu repositório → Settings → Secrets → Actions
   - New repository secret
   - Name: `COPILOT_BUSINESS_TOKEN`
   - Value: [cole o token copiado]

#### ❌ Erro Comum: Token Clássico

Se você vir este erro:
```
Error: Classic Personal Access Tokens (ghp_) are not supported by Copilot.
```

**Causa**: Você usou um token clássico (ghp_) em vez de Fine-Grained (github_pat_)

**Solução**: Siga os passos acima para criar um Fine-Grained Token

### 2. Verifique Permissões do Workflow

Certifique-se de que o workflow tem permissões para criar PRs:

1. Vá em: **Settings** → **Actions** → **General**
2. Em **Workflow permissions**, selecione:
   - ✅ **Read and write permissions**
   - ✅ **Allow GitHub Actions to create and approve pull requests**

## 🚀 Como Executar

### Passo 1: Acesse Actions

1. Vá na aba **Actions** do seu repositório
2. Selecione o workflow: **🤖 Copilot CLI Agent (Business Plan) - File Editor**
3. Clique em **Run workflow**

### Passo 2: Configure os Parâmetros

#### **target_files** (Padrão de arquivos)
Especifica quais arquivos processar:
- `*.py` - Todos os arquivos Python na raiz
- `**/*.py` - Todos os arquivos Python no repositório
- `*.yaml` - Todos os arquivos YAML
- `scripts/*.py` - Python apenas na pasta scripts

**Padrão**: `*.py`

#### **instruction** (Instrução para o agente)
O que você quer que o agente faça:
- `"Adicione comentários técnicos explicativos em português"`
- `"Adicione docstrings completas em todas as funções"`
- `"Refatore o código seguindo PEP 8"`
- `"Adicione tratamento de erros em todas as funções"`

**Padrão**: `"Adicione comentários técnicos explicativos em português"`

#### **max_files** (Máximo de arquivos)
Quantos arquivos processar por execução:
- `10` - Para testes rápidos
- `20` - Padrão recomendado
- `50` - Para processar muitos arquivos

**Padrão**: `20`

#### **model** (Modelo de IA)
Escolha o modelo do Copilot Business:
- `claude-sonnet-4.5` - Mais avançado (recomendado)
- `claude-3.5-sonnet` - Alternativa
- `gpt-4` - OpenAI GPT-4
- `gpt-4-turbo` - GPT-4 mais rápido

**Padrão**: `claude-sonnet-4.5`

### Passo 3: Execute

Clique em **Run workflow** para iniciar.

## 📊 O Que Acontece Durante a Execução

### Fase 1: Setup e Verificação ✅
- ✅ Faz checkout do repositório
- ✅ Instala Python 3.11
- ✅ Instala GitHub Copilot CLI
- ✅ Autentica com plano Business
- ✅ **Verifica e mostra que está usando plano Business**
- ✅ Lista modelos disponíveis

### Fase 2: Configuração do Agente ⚙️
- ⚙️ Define modelo escolhido (Claude Sonnet 4.5)
- ⚙️ Configura temperatura e max_tokens
- ⚙️ Escaneia arquivos do repositório
- ⚙️ Lista arquivos que serão processados

### Fase 3: Edição de Arquivos 🤖
- 🤖 Processa cada arquivo individualmente
- 🤖 Envia arquivo + instrução para o agente
- 🤖 **Agente edita o arquivo diretamente**
- 🤖 Salva as alterações
- 🤖 Mostra progresso em tempo real

### Fase 4: Commit e PR 🚀
- 📊 Mostra resumo das alterações
- 🔀 Cria branch automática
- 💾 Faz commit com mensagem detalhada
- 🚀 Cria Pull Request automático
- 📝 Gera summary com estatísticas

## 📈 Entendendo os Resultados

### No Log da Action

Você verá algo como:

```
═══════════════════════════════════════
🔍 VERIFICANDO PLANO COPILOT BUSINESS
═══════════════════════════════════════

📊 Status da conta:
✅ Logged in to GitHub Copilot (Business Plan)

✨ Features disponíveis:
- Model: claude-sonnet-4.5
- Max tokens: 8000
- Temperature: 0.3

🤖 Modelos disponíveis:
- GPT-4, GPT-4 Turbo, Claude Sonnet (Business)

═══════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 Processando: scripts/generate_summary.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✅ Arquivo modificado pelo agente

═══════════════════════════════════════
✨ EDIÇÃO CONCLUÍDA
═══════════════════════════════════════
📊 Arquivos modificados: 5
```

### No Pull Request

Será criado um PR com:
- Título: `🤖 Copilot Agent: [sua instrução]`
- Descrição detalhada com:
  - Plano usado (Business)
  - Modelo usado (Claude Sonnet 4.5)
  - Instrução executada
  - Número de arquivos processados
  - Lista de arquivos modificados

### No Summary

Veja um relatório completo em **Actions** → (sua execução) → **Summary**

## 🎯 Exemplos de Uso

### Exemplo 1: Adicionar Documentação

```yaml
target_files: "**/*.py"
instruction: "Adicione docstrings detalhadas em todas as funções e classes seguindo PEP 257"
max_files: 30
model: claude-sonnet-4.5
```

### Exemplo 2: Melhorar Testes

```yaml
target_files: "tests/**/*.py"
instruction: "Adicione casos de teste adicionais e assertions mais detalhadas"
max_files: 15
model: gpt-4-turbo
```

### Exemplo 3: Refatorar YAML

```yaml
target_files: "**/*.yaml"
instruction: "Adicione comentários explicativos em cada seção e melhore a organização"
max_files: 10
model: claude-sonnet-4.5
```

### Exemplo 4: Melhorar JavaScript

```yaml
target_files: "src/**/*.js"
instruction: "Adicione JSDoc completo e comentários explicativos em funções complexas"
max_files: 20
model: claude-3.5-sonnet
```

## 🔍 Verificação do Plano Business

O workflow **garante** que está usando o plano Business através de:

1. **Secret específico**: `COPILOT_BUSINESS_TOKEN`
2. **Verificação de status**: Step que mostra o plano ativo
3. **Listagem de modelos**: Mostra modelos disponíveis (Business tem mais)
4. **Modelo Claude Sonnet**: Só disponível em planos Business
5. **Summary report**: Mostra explicitamente "Copilot Business"

## ⚠️ Troubleshooting

### ❌ Erro: "Authentication failed" com Fine-Grained Token

**Mensagem completa**:
```
Error: Authentication failed (Request ID: ...)
If using a Fine-Grained PAT, ensure it has the 'Copilot Requests' permission enabled
```

**Causa**: Token Fine-Grained está correto, mas **falta a permissão de Copilot**

**Solução**:

1. **Acesse seus tokens**: https://github.com/settings/tokens

2. **Encontre seu token** "Copilot Business Token" e clique nele

3. **Role até o FINAL da página** para encontrar **"Account permissions"**
   - ⚠️ NÃO confunda com "Repository permissions" (que fica no topo)
   - "Account permissions" fica mais abaixo, quase no final

4. **Expanda "Account permissions"** e procure por:
   - **Copilot Chat**: Selecione `Read and write` ou `Read`
   - OU
   - **Copilot**: Selecione `Read`

5. **Clique em "Update token"** no final da página

6. **Execute o workflow novamente**

**Dica**: Se você não vê as opções de Copilot em Account permissions, sua conta pode não ter acesso ao Copilot Business. Verifique com seu administrador.

### ❌ Erro: "refusing to allow a Personal Access Token to create or update workflow without `workflow` scope"

**Mensagem completa**:
```
! [remote rejected] copilot-agent/edits-xxx -> copilot-agent/edits-xxx 
(refusing to allow a Personal Access Token to create or update workflow 
`.github/workflows/IA-ACTION.yaml` without `workflow` scope)
```

**Causa**: O agente tentou editar arquivos em `.github/workflows/` mas o token não tem permissão `Workflows`

**Solução**:

1. **Acesse seus tokens**: https://github.com/settings/tokens

2. **Encontre seu token** "Copilot Business Token" e clique para editar

3. **Role até "Repository permissions"**

4. **Encontre "Workflows"** e configure:
   - ✅ **Workflows**: `Read and write`

5. **Clique em "Update token"** no final da página

6. **Execute o workflow novamente**

**Alternativa**: Se você NÃO quer que o agente edite workflows:
- Modifique a instrução para excluir arquivos `.github/workflows/`
- Exemplo: "Adicione comentários em todos os arquivos Python, mas não edite workflows"

### ❌ Erro: "Classic Personal Access Tokens (ghp_) are not supported by Copilot"

**Causa**: Você está usando um token clássico em vez de Fine-Grained

**Solução**:
1. Acesse: https://github.com/settings/tokens?type=beta
2. Crie um **Fine-Grained Token** (não Classic)
3. Configure as permissions conforme instruções acima
4. Substitua o secret `COPILOT_BUSINESS_TOKEN` com o novo token
5. O novo token deve começar com `github_pat_` (não `ghp_`)

### Erro: "COPILOT_BUSINESS_TOKEN não encontrado"

**Solução**: Configure o secret conforme instruções acima

### Erro: "Modelo não disponível"

**Solução**: 
1. Verifique se seu plano Business tem acesso ao modelo
2. Tente outro modelo (gpt-4, gpt-4-turbo)
3. Verifique o log de verificação do plano

### Erro: "Permission denied"

**Solução**: 
1. Verifique as permissões do workflow (Settings → Actions → General)
2. Certifique-se que o token tem as permissions corretas:
   - Contents: Read and write
   - Pull requests: Read and write

### Nenhum arquivo encontrado

**Solução**: 
1. Verifique o padrão em `target_files`
2. Veja o log do step "Scan Repository Files"
3. Use padrões mais abrangentes como `**/*.py`

### Agente não retornou conteúdo

**Solução**:
1. Simplifique a instrução
2. Reduza o tamanho dos arquivos
3. Tente outro modelo

## 📚 Recursos Adicionais

- [GitHub Copilot CLI](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Copilot Business](https://docs.github.com/en/copilot/overview-of-github-copilot/about-github-copilot-business)

## 💡 Dicas

- ✅ Comece com poucos arquivos (max_files: 5-10) para testar
- ✅ Use instruções específicas e claras
- ✅ Revise sempre o PR antes de fazer merge
- ✅ Claude Sonnet 4.5 é geralmente melhor para código
- ✅ GPT-4 Turbo é mais rápido mas pode ser menos preciso
- ✅ Sempre verifique o log para confirmar o plano Business

---

**Criado com 🤖 GitHub Copilot (Business Plan)**
