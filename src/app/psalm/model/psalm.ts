
export class Psalm {
    name: string;
    effect: string;
    successor: Psalm[];     //this is made of successor
    predecessor:  Psalm[];  //this can be used to craft predecessor


    constructor( name: string, effect: string) {
        this.name = name;
        this.effect = effect;
        this.successor = [];
        this.predecessor = [];

    }
    
    public getImgFile(): string {
        return 'assets/img/' + this.getId() + '.png';
    }
    
    public getId(): string {
        return this.name.toLowerCase().replace(' psalm', '');
    }
}
