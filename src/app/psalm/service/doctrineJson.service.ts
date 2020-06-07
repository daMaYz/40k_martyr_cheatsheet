import { Injectable, Inject, Optional, ReflectiveInjector, Injector } from '@angular/core';
import { Observable } from 'rxjs';

import { Doctrine } from '@app/psalm/model/doctrine';
import {PsalmJsonService} from './psalmJson.service'

import * as jsonData from '@assets/data/doctrine.json';


@Injectable( { providedIn: 'root' } )
export class DoctrineJsonService {
    private psalmJsonService: any;
    static doctrineList: Doctrine[] = [];

    constructor(psalmJsonService: PsalmJsonService){
        this.psalmJsonService = psalmJsonService;
    }
    
    init() {
        // load basic data from json
        for(let key in jsonData['default']) {
            let data = jsonData['default'][key];
            let doc = new Doctrine(data['effect']);
            doc.children = [];
            // children
            for(let i in data['children']) {
                doc.children.push(this.psalmJsonService.getByName(data['children'][i]));
            }
            DoctrineJsonService.doctrineList.push(doc);
        }
        console.log('Loaded', DoctrineJsonService.doctrineList.length, 'Psalms from assets/data/doctrine.json:', DoctrineJsonService.doctrineList);
    }
    
    private registerChildren(children: string[]) {
    }
    
    getAll():Doctrine[] {
        if(DoctrineJsonService.doctrineList.length ===  0) {
            this.init();
        }
        return DoctrineJsonService.doctrineList;
    }
}