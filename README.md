<h2>RESTful API with FLASK</h2>
<h3>Intro</h3>
<ul>
  <li>A RESTful API uses HTTP requests to help a client (web or mobile app) to interact with server's database.</li>
  <li>HTTP requests (GET, PUT, POST or DELETE) allow for inserting, deleting, updating or retrieving data in db.</li>
  <li>With RESTful API in Flask, I can define the way of interaction between client and server - all via HTTP requests.</li>
  <li>Here is an example of a client sending POST request with data to server through API:</li>
</ul>

<image src="images/api_schema.JPG">

<ul>
  <li>The representation of a relational database to API is <b>Python Data Model</b>.</li>
  <li>The representation of Python Data Model to client App is a defined within API <b>Resource</b> of a specific Model.</li>
  <li>For each specific Data Model we need to define separate API Resource: For TransactionModel there is need to define Transaction API Resource. The same for payers: for PayerModel there is need to define Payer API Resource.</li>
  <li>Resource is an external representation of internal Model.</li>
  <li>Client App can access Python object of given Model only thorugh API Resource.</li>
  <li>Client App can interact with Resource using HTTP requests.</li>
  <li>With that solution, API Resource deciedes what Model objects are accessible and in what way id est getting, posting, putting, deleting.</li>
</ul>


<h3>Testing HTTP methods and RESTful API</h3>
<ul>
  <li>Project has been written along with automated testing.</li>
  <li>With testing we can check the Client-API-Server performance.</li>
</ul>
<image src="images/test.JPG">
  
<h3>Database</h3>

<ul>
  <li>Payers db table.</li>
  <li>Every single table row represents a single Python object of the PayerModel class.</li>
  <li>Table attributes (headings) represent properties of PayerModel type object .</li>
</ul>
<image src="images/payers_table.JPG">
  
<ul>
  <li>Transaction db table.</li>
  <li>Every single table row represents a single Python object of the TransactionModel class.</li>
  <li>Table attributes (headings) represent properties of TransactionModel type object.</li>
</ul>
<image src="images/transaction_table.JPG">
  
  
<h3>Ad-hoc SQL Analysis</h3>
<ul>
  <li>Client classification as per transaction amount.</li>
</ul>
<image src="images/client_clasification.JPG">
 <ul>
  <li>Getting second biggest transaction.</li>
</ul>
<image src="images/second biggest amount.JPG"">
<ul>
  <li>Currency count.</li>
</ul>
<image src="images/currency_count.JPG">
                                      
                                      
<h3>Cmd</h3>
<ul>
  <li>By importing db I can opearte on a database treating records as the objects:</li>
</ul>
<image src="images/cmd.JPG">
