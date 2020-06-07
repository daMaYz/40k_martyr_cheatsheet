import { Component, OnInit, Input } from '@angular/core';

import { Psalm } from '@app/psalm/model/psalm';
import { PsalmJsonService } from '@app/psalm/service/psalmJson.service';

@Component( {
    selector: 'psalmOverview',
    templateUrl: './psalmOverview.component.html'
} )
export class PsalmOverviewComponent implements OnInit {

    public allPsalms: Psalm[] = [];
    public filteredPsalms: Psalm[] = [];


    constructor(
        private psalmJsonService: PsalmJsonService,
    ) { }

    ngOnInit(): void {
        this.allPsalms = Array.from( this.psalmJsonService.getAll().values() );
        this.init();
    }

    init() {
        console.log( 'this.allPsalms:', this.allPsalms );
        this.filteredPsalms = this.allPsalms;
    }

    private activeFilter = {
        'name': '',
        'effect': ''
    };
    filter( text: string, column: string ) {
        this.activeFilter[column] = text;

        this.filteredPsalms = this.allPsalms.filter(
            psalm => {
                return psalm.name.toLowerCase().includes( this.activeFilter['name'].toLowerCase() ) &&
                    psalm.effect.toLowerCase().includes( this.activeFilter['effect'].toLowerCase() );
            }
        );
    }
}
