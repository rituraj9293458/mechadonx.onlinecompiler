This project is the prototye i was working with.
Initially i was thinking of using a local model deepseek 8b and qwen 7b coder where the deepseek model managed to analyse the code and mark the errors+suggestions and the writter was supposed to simpley do what the suggestions said
issues faced:the deepseek model being a reasoning model created a lot of thinking tags which caused the parser to throw error i tried to optimise the output using prompt but that caused a lot of time and errors
then i used qwen coder 7b as both the analyser and the writter this caused the code being not analysed properly as coder is just a coding part which i wasn't thinking of using to analyse also it sucks at analysing
then i moved to granite 8b which being a model optimized for coding i considered as the perfect choice 
issues faced here wasnt able to reason properly with the time complexity like it wasn't making the perfectcode field as false which was needed to pass the code and everything to the writter/qwen coder
Final sollution:gemini api key used to use gemini 3.6flash-lite perfect code execution and i also put a condition that if the code is rewritten 3 times gemini will take the mantel and convert the code 


primarily this didnt work how i wanted next stages will be to use two local models to optimse and produce a more optimised code compared to using a simple one model or other thing but i failed gotta make some other things like fine tuning
or something other 


stage 1 was to make the backend analysing part which i will be using in the online code compiler and else but since this failed gotta think of something else Ya but the code still works no issues but the thing i wanted wasnt achieved



stage-2 will be to make the backend and frontend of the online compiler
and also i am learning things from scratch so its taking time


stage 3 will be to use docker and other things like monaco to make a vs code clone and host it using cloudflare tunnening and vercel will probably do later
