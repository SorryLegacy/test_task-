
<h1>first task </h1><br>
<code>select client_number as client,(select count(outcome) as win
from bid join event_value on bid.play_id = event_value.play_id  
where outcome = 'win' and event_value.play_id = bid.play_id and bid.client_number = client ) as win,
(select count(outcome) as lose
from bid join event_value on bid.play_id = event_value.play_id  
where outcome = 'lose' and event_value.play_id = bid.play_id and bid.client_number = client ) as lose
from bid
group by client_number</code>
<br>
<h1>second task </h1>
<code>select home_team as ht , away_team as ate ,(select count(play_id) from event_entity
where home_team = ht and away_team = ate or away_team = ht and home_team = ate ) as count
from event_entity </code>
