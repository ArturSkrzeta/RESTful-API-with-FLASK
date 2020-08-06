<h2>RESTful API with FLASK</h2>
<h3>Intro</h3>
<ul>
  <li>A RESTful API is the Application Program Interface that uses HTTP requests (GET, PUT, POST or DELETE) to help a client (web or mobile app) to interact with server's database - inserting or retrieving data.</li>
  <li>With RESTful API in Flask, I can define the way of interaction between client and server - all via HTTP requests.</li>
</ul>
<image src="images/api_schema.JPG">


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
