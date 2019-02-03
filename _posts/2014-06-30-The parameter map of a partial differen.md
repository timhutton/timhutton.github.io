---
layout: post
title: The parameter map of a partial differen
---

<html><head><meta charset="utf-8"><title>The parameter map of a partial differential equation, showing a reasonably st...</title><style>body {font: 11pt Roboto, Arial, sans-serif; max-width: 640px; margin: 24px;}.author-photo {border-radius: 50%; margin-right: 10px; width: 40px;}.author {font-weight: 500;}.main-content {margin: 15px 0 15px;}.post-title {font-weight: bold;}.location {display: block; margin-top: 15px;}.location img {float: left; margin-right: 5px; width: 20px;}.media-link {display: inline-block; max-width: 100%; vertical-align: top;}.media-link p {margin-top: 5px; max-height: 4em; overflow: scroll;}.media {max-height: 100vh; max-width: 100%;}.video-placeholder {background: black; display: flex; height: 300px; max-width: 100%; width: 640px;}.play-icon {border-bottom: 30px solid transparent; border-left: 50px solid white; border-top: 30px solid transparent; color: white; margin: auto;}.album {max-height: 800px; overflow: scroll; width: calc(100vw - 48px);}.album .media-link {margin-right: 5px; max-width: 250px;}.album .media {max-height: 250px;}.link-embed {border-top: 1px solid lightgrey; display: block; margin-top: 20px;}.link-embed img {max-width: 100%;}.inline-link-embed {display: block;}.inline-link-embed img {vertical-align: middle;}.link-title {display: inline-block; font-size: medium; font-weight: 300; padding-left: 1em;}.reshare-attribution {display: block; font-weight: bold; margin-bottom: 10px;}.poll-image {margin-bottom: 5px; max-height: 300px; max-width: 500px;}.poll-choice {align-items: center; display: flex; margin-bottom: 5px; max-width: 500px;}.poll-choice-percentage {background-color: lightblue; height: 100%; left: 0; position: absolute; z-index: -1;}.poll-choice-selected {margin-right: 5px;}.poll-choice-results {border: 1px solid lightgray; border-radius: 5px; display: flex; line-height: 40px; overflow: hidden; padding: 0 8px; position: relative;}.poll-choice-results, .poll-choice-description {flex-grow: 1; margin-right: 10px;}.poll-choice-image {width: 100%;}.poll-choice-image, .poll-choice-image img {max-height: 40px; max-width: 100px;}.poll-choice-votes {max-height: 100px; overflow: auto;}.plus-entity-embed {color: black; display: block; text-decoration: none;}.plus-entity-embed-cover-photo {max-height: 300px; max-width: 100%;}.plus-entity-embed-info {padding: 0 1em 1em;}.plus-entity-embed-info h2 {font-weight: 500; margin: 10px 0;}.plus-entity-embed-info p {font-size: small; margin: 0;}.collection-owner-avatar {border-radius: 50%; border: 2px solid white; height: 40px; margin-top: -22px;}.visibility {padding: 1em 0; border-top: 1px solid grey;}.post-activity {padding: 1em 0; border-top: 1px solid grey;}.comments {border-top: 1px solid gray; padding-top: 1em;}.comment + .comment {margin-top: 1em;}.comment .media-link, .comment .inline-link-embed {margin-top: 5px;}</style></head><body><div style="margin-bottom:1em;"><div style="display:flex; align-items:center"><img class="author-photo" src="https://lh4.googleusercontent.com/-epo4ZZKNqEw/AAAAAAAAAAI/AAAAAAAAVSU/qu3LpcHEnoQ/s64-c/photo.jpg" alt="Tim Hutton"><a href="https://plus.google.com/+TimHutton" target="_blank" class="author">Tim Hutton</a> - <a target="_blank" href="https://plus.google.com/+TimHutton/posts/dnaVNGMfB2B">2014-06-30 14:04:00+0000</a><span> - Updated: 2014-07-01 08:06:58+0000</span></div><div class="main-content">The parameter map of a partial differential equation, showing a reasonably standard pattern of Turing instabilities for different combinations of parameters - spots and labyrinthine stripes. But..<br><br>The intriguing thing here is that this is a single chemical system! It doesn&#39;t fit into the usual characterisation of activator and inhibitor, like Gray-Scott or Turing&#39;s original model.<br><br>The formula is:<br><br>du/dt = mu*u - bilaplacian(u) - 2*laplacian(u) - u + beta*u*u - u*u*u<br><br>In this parameter map, mu ranges from -1 on the left to 5 on the right, and beta ranges from -3 at the bottom to 3 at the top.<br><br>The bilaplacian is the laplacian operator applied twice. In a one-dimensional system if your laplacian is computed by a finite differencing kernel of 1,-2,1 then the bilaplacian kernel is 1,-4,6,-4,1.<br><br>The formula comes from the work of <span class="proflinkWrapper"><span class="proflinkPrefix">+</span><a class="proflink bidi_isolate" href="https://plus.google.com/114072586680921496422" oid="114072586680921496422" >Matt Pennybacker</a></span>:<br><a rel="nofollow" target="_blank" href="http://pennybacker.net" class="ot-anchor bidi_isolate" jslog="10929; track:click" dir="ltr">http://pennybacker.net</a><br>(Matt suggested trying it without the gradient term in the paper.)<br><br>There are some Ready files here to explore:<br><a rel="nofollow" target="_blank" href="http://code.google.com/p/reaction-diffusion/source/browse/trunk/Ready#Ready%2FPatterns%2FPennybacker2013" class="ot-anchor bidi_isolate" jslog="10929; track:click" dir="ltr">http://code.google.com/p/reaction-diffusion/source/browse/trunk/Ready#Ready%2FPatterns%2FPennybacker2013</a></div><a href="/assets/mp_parameter_map_mu-1..1_beta-3..3.png" target="_blank" class="media-link"><img src="/assets/mp_parameter_map_mu-1..1_beta-3..3.png" alt="The parameter map of a partial differential equation, showing a reasonably standard pattern of Turing instabilities for different combinations of parameters - spots and labyrinthine stripes.



The intriguing thing here is that this is a single chemical system! It doesn&#39;t fit into the usual characterisation of activator and inhibitor, like Gray-Scott or Turing&#39;s original model.



The formula is:



du/dt = mu*u - bilaplacian(u) - 2*laplacian(u) - u + beta*u*u - u*u*u



In this parameter map, mu ranges from -1 on the left to 1 on the right, and beta ranges from -3 at the bottom to 3 at the top.



The bilaplacian is the laplacian operator applied twice. In a one-dimensional system if your laplacian is computed by a finite differencing kernel of 1,-2,1 then the bilaplacian kernel is 1,-4,6,-4,1.



The formula comes from the work of +Matt Pennybacker:

http://pennybacker.net

(Matt suggested trying it without the gradient term in the paper.)



There are some Ready files here to explore:

http://code.google.com/p/reaction-diffusion/source/browse/trunk/Ready#Ready%2FPatterns%2FPennybacker2013" class="media"><p>The parameter map of a partial differential equation, showing a reasonably standard pattern of Turing instabilities for different combinations of parameters - spots and labyrinthine stripes.



The intriguing thing here is that this is a single chemical system! It doesn&#39;t fit into the usual characterisation of activator and inhibitor, like Gray-Scott or Turing&#39;s original model.



The formula is:



du/dt = mu*u - bilaplacian(u) - 2*laplacian(u) - u + beta*u*u - u*u*u



In this parameter map, mu ranges from -1 on the left to 1 on the right, and beta ranges from -3 at the bottom to 3 at the top.



The bilaplacian is the laplacian operator applied twice. In a one-dimensional system if your laplacian is computed by a finite differencing kernel of 1,-2,1 then the bilaplacian kernel is 1,-4,6,-4,1.



The formula comes from the work of +Matt Pennybacker:

http://pennybacker.net

(Matt suggested trying it without the gradient term in the paper.)



There are some Ready files here to explore:

http://code.google.com/p/reaction-diffusion/source/browse/trunk/Ready#Ready%2FPatterns%2FPennybacker2013</p></a></div><div class="visibility">Shared with: Public, <a href="https://plus.google.com/114072586680921496422">Matt Pennybacker</a></div><div class="post-activity"><div class="plus-oners">+1'd by: <a href="https://plus.google.com/+MartinNovy1234">Martin Novy</a>, <a href="https://plus.google.com/112849295295677024268">Abdi Osman</a>, <a href="https://plus.google.com/+TorolfSauermann">Torolf Sauermann</a>, <a href="https://plus.google.com/+AistisRaulinaitis">Aistis Raulinaitis</a>, <a href="https://plus.google.com/103812300491207235218">Cassidy Curtis</a>, <a href="https://plus.google.com/+AaronHertzmann">Aaron Hertzmann</a>, <a href="https://plus.google.com/+CraigReynolds">Craig Reynolds</a>, <a href="https://plus.google.com/+ElżbietaZadoraZuzelska">Elżbieta Zadora-Zuzelska</a>, <a href="https://plus.google.com/107307517189035595443">Luc Blanchette</a>, <a href="https://plus.google.com/+RickyMooreDaniels">Ricky Moore-Daniels</a>, <a href="https://plus.google.com/102851779752853237912">Paweł Zuzelski</a>, <a href="https://plus.google.com/+ÁngelLinaresGarcía">Ángel Linares García</a>, <a href="https://plus.google.com/+FelixWoitzel">Felix Woitzel</a>, <a href="https://plus.google.com/+StepanRoucka">Štěpán Roučka</a>, <a href="https://plus.google.com/+HectorYee">Hector Yee</a>, <a href="https://plus.google.com/+KevinOBryant">Kevin O&#39;Bryant</a>, <a href="https://plus.google.com/+HunterYavitz">Hunter Yavitz</a>, <a href="https://plus.google.com/+SebastianFernandezAlberdi">Sebastian Fernandez Alberdi</a>, <a href="https://plus.google.com/+DanWills">Dan Wills</a>, <a href="https://plus.google.com/+DylanLeigh">Dylan Leigh</a>, <a href="https://plus.google.com/+DaveGordon0">Dave Gordon</a>, <a href="https://plus.google.com/+KevinC">Kevin C.</a>, <a href="https://plus.google.com/114760333857631915709">kenny bell</a>, <a href="https://plus.google.com/+DanielAmmannCH">Daniel Ammann</a>, <a href="https://plus.google.com/+OwenMaresh">Owen Maresh</a>, <a href="https://plus.google.com/111750881748363551870">Doug Hackworth</a>, <a href="https://plus.google.com/+AllanMedeiros">allan de medeiros martins</a>, <a href="https://plus.google.com/+EmilMikulic">Emil Mikulic</a>, <a href="https://plus.google.com/+ScottVorthmann">Scott Vorthmann</a></div><div class="resharers">Reshared by: <a href="https://plus.google.com/+MartinNovy1234">Martin Novy</a>, <a href="https://plus.google.com/+EvelynMitchell">Evelyn Mitchell</a>, <a href="https://plus.google.com/+MosheVardi">Moshe Vardi</a>, <a href="https://plus.google.com/+LeeNelsontechnologiclee">Lee Nelson</a>, <a href="https://plus.google.com/112237796514671545656">Alberto Pereira</a>, <a href="https://plus.google.com/102851779752853237912">Paweł Zuzelski</a>, <a href="https://plus.google.com/+FelixWoitzel">Felix Woitzel</a>, <a href="https://plus.google.com/+DaveGordon0">Dave Gordon</a>, <a href="https://plus.google.com/+MirkoBulaja">Mirko Bulaja</a>, <a href="https://plus.google.com/+StephenMercer">Stephen Loftus-Mercer</a></div></div><div class="comments"><div class="comment"><a target="_blank" href="https://plus.google.com/+DanWills" class="author">Dan Wills</a><span class="time"> - 2014-07-01 01:51:39+0000</span><div class="comment-content">Wow Tim that is bloody interesting! Thanks for sharing, both to yourself and Matt Pennybacker!</div></div><div class="comment"><a target="_blank" href="https://plus.google.com/+ChristopherHanusa" class="author">Christopher Hanusa</a><span class="time"> - 2014-07-01 02:27:14+0000</span><div class="comment-content">This makes me think about a random grove: <a rel="nofollow" target="_blank" href="http://arxiv.org/abs/math/0407171" class="ot-anchor bidi_isolate" jslog="10929; track:click" dir="ltr">http://arxiv.org/abs/math/0407171</a><br>(See page 10).  I wonder if it is at all related.</div></div><div class="comment"><a target="_blank" href="https://plus.google.com/+FelixWoitzel" class="author">Felix Woitzel</a><span class="time"> - 2014-07-01 06:46:55+0000</span><div class="comment-content">it&#39;s really reminiscent of <a rel="nofollow" target="_blank" href="http://mrob.com/pub/comp/xmorphia/index.html" class="ot-anchor bidi_isolate" jslog="10929; track:click" dir="ltr">http://mrob.com/pub/comp/xmorphia/index.html</a> - good job! </div></div><div class="comment"><a target="_blank" href="https://plus.google.com/110065069221457596291" class="author">Lewpen Kinross-Skeels</a><span class="time"> - 2014-07-16 20:56:58+0000</span><div class="comment-content">Beautiful!</div></div></div></body></html>

<i>This post was originally on Google+</i>