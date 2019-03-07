
class Game{
    constructor(){
        this.Money = 100000;
        this.Workers = [];
        this.Weeks = 52;
        this.GameOver = false;
        this.ProjectProgress = 0;

        //TODO: prendre une ref sur les Labels pour l'affichage des Valeurs
    }

    Tick(){
        if(this.Money < 0 ||  this.Weeks <= 0){
            this.GameOver = true;
            GameOver();
        }else{

            for (const worker in this.Workers) {
                worker.Tick()

            }
            
            if(this.ProjectProgress >= 100){
                GameOver();
            }
            this.Weeks-=1;

        }

        // TODO: Faire un Update de UI avec les nouvelles Valeurs

    }

    GameOver(){
        if(this.ProjectProgress >= 100 && this.Money >= 0 && this.Weeks >= 0){ 
            //Win

        }else{ 
            //Lose

        }
    }
}

class Worker{
    constructor(game,startingValue,NbWeeksStarting,FinalValue){
        this.WeekCount = 0;
        this.Game = game;
        this.BaseValue = startingValue;
        this.WeekBaseValue = NbWeeksStarting;
        this.FinalValue = FinalValue;
    }

    Tick(){
        this.WeekCount += 1;
        if(this.WeekCount >= this.WeekBaseValue)
        {
            this.Game.ProjectProgress += this.FinalValue;
        }else{
            this.Game.ProjectProgress += this.BaseValue;
        }
    }
}

//Game Instance
var GameInstance = new Game();

function AddWorker(Price, BaseValue, NbWeekBase, FinalValue) { // Value set dans le OnClick du bouton (HTML)
    if(GameInstance.Money >= Price){
        GameInstance.Money -= Price;
        GameInstance.Workers.push(new Worker(GameInstance,BaseValue,NbWeekBase,FinalValue));
    }
}

function NextWeek() {
    if(!GameInstance.GameOver){
        GameInstance.Tick();
    }
}

function SubContract() {
    if(GameInstance.Money >= 2000){
        GameInstance.Money -= 2000;
        GameInstance.ProjectProgress += (Rand()%6)+1; //Fix Random
    }
}