import { Component, OnInit, Input } from '@angular/core';

import { Psalm } from '@app/psalm/model/psalm';
import { Doctrine } from '@app/psalm/model/doctrine';
import { PsalmJsonService } from '@app/psalm/service/psalmJson.service';
import { DoctrineJsonService } from '@app/psalm/service/doctrineJson.service';

@Component( {
    selector: 'doctrineOverview',
    templateUrl: './doctrineOverview.component.html'
} )
export class DoctrineOverviewComponent implements OnInit {

    public allDoctrines: Doctrine[] = [];
    public filteredDoctrines: Doctrine[] = [];


    constructor(
            private psalmJsonService: PsalmJsonService,
            private doctrineJsonService: DoctrineJsonService,
    ) { }

    ngOnInit(): void {
        this.allDoctrines = Array.from( this.doctrineJsonService.getAll().values() );
        this.init();
    }

    init() {
        this.filteredDoctrines = this.allDoctrines;
    }

    private activeFilter = {
        'effect': '',
        'subEffect': '',
        'children': ''
    };
    filter( text: string, column: string ) {
        this.activeFilter[column] = text;

        this.filteredDoctrines = this.allDoctrines.filter(
            doc => {
                let subFilter = false;
                let childrenFilter = false;
                
                for(let child of doc.children) {
                    if(child.effect.toLowerCase().includes( this.activeFilter['subEffect'].toLowerCase())) {
                        subFilter = true;
                        break;
                    }
                }
                
                for(let child of doc.children) {
                    if(child.name.toLowerCase().includes( this.activeFilter['children'].toLowerCase())) {
                        childrenFilter = true;
                        break;
                    }
                }
                
                return doc.effect.toLowerCase().includes( this.activeFilter['effect'].toLowerCase())
                        && subFilter && childrenFilter;
            }
        );
    }
}
