class Game{
    constructor(){
        this.Init();
    }
    Init() {
        this.Money = 100000;
        this.Workers = [];
        this.Weeks = 52;
        this.isGameOver = false;
        this.ProjectProgress = 0;
        this.earlyAccess = false;
        this.earlyAccessWeeks = 0;

        //TODO: prendre une ref sur les Labels pour l'affichage des Valeurs
        document.getElementById("office").innerHTML="";
        this.weekNode = document.getElementById("weekNumber");
        this.progressNode = document.getElementById("progress");
        this.budgetNode = document.getElementById("budget");
        this.budgetNode.innerHTML = this.Money;
        this.UpdateUI();
    }
    Reset() {
        this.Init();
    }

    Tick(){
        if(this.Money < 0 ||  this.Weeks <= 0){
            this.isGameOver = true;
            this.GameOver();
        }else{
            this.Workers.forEach((worker) => {
                worker.Tick()
            })

            if(this.ProjectProgress >= 100){
                this.ProjectProgress = 100;
                this.GameOver();
            }
            this.Weeks-=1;
            if(this.earlyAccess){
              this.Money -= this.earlyAccessWeeks * 1000;
              this.earlyAccessWeeks += 1;

            }
        }
        this.UpdateUI();
    }

    UpdateUI() {
        // TODO: Faire un Update de UI avec les nouvelles Valeurs
        this.weekNode.innerHTML = 52-this.Weeks;
        this.progressNode.innerHTML = this.ProjectProgress;
        this.budgetNode.innerHTML = this.Money;
    }

    GameOver(){
        if(this.ProjectProgress >= 100 && this.Money >= 0 && this.Weeks >= 0){
            //TODO: Win
            alert("You win!")
            this.Reset();

        }else{
            //TODO: Lose
            alert("You lose!")
            this.Reset();

        }
    }
}

class Worker{
    constructor(game,startingValue,NbWeeksStarting,FinalValue, type){
        this.WeekCount = 0;
        this.Game = game;
        this.BaseValue = startingValue;
        this.WeekBaseValue = NbWeeksStarting;
        this.FinalValue = FinalValue;
        this.type = type;
        this.image = document.createElement("img");
        // TODO: support programmer & tester
        if (type == 'programmer') {
            this.image.src= "assets/programmer.png";
        } else {

            this.image.src= "assets/tester.png";
        }
        document.getElementById("office").appendChild(this.image);
    }

    Tick(){
        this.WeekCount += 1;
        if(this.WeekCount >= this.WeekBaseValue)
        {
            this.Game.ProjectProgress += this.FinalValue;
        }else{
            this.Game.ProjectProgress += this.BaseValue;
        }
        if (this.type == 'programmer') {
            this.Game.Money -= 1200;
        } else {
            this.Game.Money -= 800;
        }
    }
}

//Game Instance
var GameInstance = new Game();

function AddWorker(Price, BaseValue, NbWeekBase, FinalValue, type) { // Value set dans le OnClick du bouton (HTML)
    if(GameInstance.Money >= Price){
        GameInstance.Money -= Price;
        worker = new Worker(GameInstance,BaseValue,NbWeekBase,FinalValue, type);
        GameInstance.Workers.push(worker);
        GameInstance.UpdateUI();
    }
}

function NextWeek() {
    if(!GameInstance.isGameOver){
        GameInstance.Tick();
    }
}

function SubContract() {
    if(GameInstance.Money >= 2000){
        GameInstance.Money -= 2000;
        console.log(GameInstance.ProjectProgress)
        GameInstance.ProjectProgress +=  Math.floor(Math.random() * Math.floor(5)) + 1//TODO: Fix Random
        GameInstance.UpdateUI();

    }
}

function EarlyAccess() {
    if(!GameInstance.earlyAccess){
      GameInstance.earlyAccess = true;
      GameInstance.Money += 15000;
      GameInstance.UpdateUI();
  }
}

function DetailedBugdet() {
  var n_programmers = 0
  var n_testers = 0;
  for(var i = 0; i < GameInstance.Workers.length; ++i){
      if(GameInstance.Workers[i].type == 'programmer'){
          n_programmers++;
      }else {
          n_testers++;
      }
  }
    alert('Balance:' + GameInstance.Money +
      "\nProgrammer's cost: " + 1200* n_programmers +
      "\nTester's cost: " + 800 * n_testers
    )
}
