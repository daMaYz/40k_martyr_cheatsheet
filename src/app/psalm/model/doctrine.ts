import { Psalm } from './psalm'

export class Doctrine {
    static doctrineList: Doctrine[] = [];

    effect: string;
    children: Psalm[];     //Nachfolger

    constructor( effect: string) {
        this.effect = effect;
        
        Doctrine.doctrineList.push(this);
    }
    
}
