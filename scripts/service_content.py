"""Public service copy; no client configuration or private operational data."""
SERVICES = {
 'custom-software': {
  'title': ('Desenvolvimento de software sob medida', 'Custom software development'),
  'intro': ('Sistemas web, APIs e integrações para os processos da sua empresa. A Moca acompanha o projeto da definição do problema à evolução do produto.', 'Web systems, APIs and integrations for your business processes. Moca works with you from defining the problem to evolving the product.'),
  'heading': ('Software que acompanha sua operação.', 'Software built around your operations.'),
  'items': [
   (('Sistemas e aplicações web', 'Web systems and applications'), ('Transformamos necessidades de negócio em fluxos de uso, interfaces e regras de operação. O escopo começa pelo que sua equipe precisa resolver.', 'We turn business needs into user flows, interfaces and operational rules. Scope starts with what your team needs to solve.')),
   (('APIs e integrações', 'APIs and integrations'), ('Conectamos aplicações e organizamos a troca de informações entre sistemas, reduzindo tarefas manuais e duplicação de dados.', 'We connect applications and organize information exchange between systems to reduce manual tasks and duplicated data.')),
   (('Entregas e evolução', 'Delivery and evolution'), ('Definimos prioridades, construímos em etapas e validamos as entregas com você. Testes e acompanhamento orientam a evolução da solução.', 'We define priorities, build incrementally and validate deliveries with you. Testing and follow-up guide the solution’s evolution.'))],
  'evidence': ('Conheça o TOODA, projeto com participação técnica da Moca voltado à proteção e ao auxílio na localização de pessoas vulneráveis. É um exemplo de tecnologia aplicada a uma necessidade concreta.', 'Explore TOODA, a project with Moca’s technical participation focused on protecting and helping locate vulnerable people. It is an example of technology addressing a concrete need.')
 },
 'metabase-bi': {
  'title': ('BI e dashboards com Metabase', 'BI and dashboards with Metabase'),
  'intro': ('Organize os dados da sua operação em relatórios que sua equipe consegue consultar. A Moca trabalha com implantação do Metabase, integração de dados e relatórios dentro de aplicações.', 'Organize operational data into reports your team can use. Moca works on Metabase deployment, data integration and reports embedded in applications.'),
  'heading': ('Da informação dispersa à consulta diária.', 'From scattered information to everyday reporting.'),
  'items': [
   (('Implantação do Metabase', 'Metabase deployment'), ('Preparamos a estrutura para conectar fontes de dados e organizar consultas e painéis, de acordo com as necessidades do projeto.', 'We prepare the infrastructure to connect data sources and organize queries and dashboards around project needs.')),
   (('Integração de dados', 'Data integration'), ('Estruturamos rotinas que levam dados dos sistemas para análise. A definição dos indicadores vem antes da construção dos relatórios.', 'We build routines that prepare system data for analysis. Defining indicators comes before building reports.')),
   (('Relatórios na aplicação', 'In-app reporting'), ('Integramos painéis à área administrativa, com controle de acesso, para que a equipe consulte informações no ambiente em que já trabalha.', 'We integrate dashboards into administrative interfaces with access controls, so teams can consult information where they already work.'))],
  'evidence': ('Nossa experiência inclui trabalhos com Metabase para TOODA e Bluesphere. Na Bluesphere, o projeto inclui relatórios integrados à área administrativa e preparação de dados de assinaturas para análise. No TOODA, realizamos trabalho de implantação do Metabase.', 'Our experience includes Metabase work for TOODA and Bluesphere. The Bluesphere project includes reports embedded in the administrative interface and subscription data preparation for analysis. For TOODA, our work includes Metabase deployment.')
 }
}


def service_body(locale, base, slug):
 p = SERVICES[slug]; i = 0 if locale == 'pt' else 1
 cards = ''.join(f'<article><span class="number">0{n+1} /</span><h3>{title[i]}</h3><p>{text[i]}</p></article>' for n, (title, text) in enumerate(p['items']))
 return f'''<section class="page-hero"><div class="wrap"><a class="breadcrumb" href="{base}#solutions">← {'Soluções' if i==0 else 'Solutions'}</a><p class="eyebrow">Moca · {'Serviços' if i==0 else 'Services'}</p><h1>{p['title'][i]}</h1><p class="lead">{p['intro'][i]}</p><a class="button" href="#contact">{'Converse sobre seu projeto' if i==0 else 'Discuss your project'} ↗</a></div></section><section class="section light"><div class="wrap"><h2>{p['heading'][i]}</h2><div class="product-features">{cards}</div></div></section><section class="section"><div class="wrap"><h2>{'Experiência em projetos reais' if i==0 else 'Experience in real projects'}</h2><p class="lead">{p['evidence'][i]}</p><a class="text-link" href="{base}products/tooda/">{'Conheça o TOODA' if i==0 else 'Explore TOODA'} ↗</a></div></section>'''
