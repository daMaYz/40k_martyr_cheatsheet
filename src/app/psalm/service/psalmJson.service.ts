import { Injectable, Inject, Optional, ReflectiveInjector, Injector } from '@angular/core';
import { Observable } from 'rxjs';

import { Psalm } from '@app/psalm/model/psalm';

import * as jsonData from '@assets/data/psalm.json';


@Injectable( { providedIn: 'root' } )
export class PsalmJsonService {
    private static psalmList = new Map<string, Psalm>();

    constructor(){
    }
    
    init() {
        // load basic data from json
        for(let key in jsonData['default']) {
            let data = jsonData['default'][key];
            let psalm = new Psalm(data['name'],  data['effect']);
            
            PsalmJsonService.psalmList.set(psalm.getId(), psalm);
        }

        // initialize parent/child dependencies
        for(let key in jsonData['default']) {
            let data = jsonData['default'][key];
            let psalm = PsalmJsonService.psalmList.get(data['name'].toLowerCase().replace(' psalm', ''));
            
            for(let i in data['successor']) {
                psalm.successor.push(this.getByName(data['successor'][i]));
            }
            for(let i in data['predecessor']) {
                psalm.predecessor.push(this.getByName(data['predecessor'][i]));
            }
        }
        console.log('Loaded', PsalmJsonService.psalmList.size, 'Psalms from assets/data/psalm.json:', PsalmJsonService.psalmList);
    }
    
    getByName(name: string): Psalm {
        if(PsalmJsonService.psalmList.size ===  0) {
            this.init();
        }
        let foundPsalm = null;
        PsalmJsonService.psalmList.forEach((psalm: Psalm, id: string) => {
            if(psalm.name === name) {
                foundPsalm = psalm;
            }
        });
        return foundPsalm;
    }
    
    getById(id: string): Psalm {
        if(PsalmJsonService.psalmList.size ===  0) {
            this.init();
        }
        return PsalmJsonService.psalmList.get(id);
    }
    
    getAll(): Map<string, Psalm> {
        if(PsalmJsonService.psalmList.size ===  0) {
            this.init();
        }
        return PsalmJsonService.psalmList;
    }
}