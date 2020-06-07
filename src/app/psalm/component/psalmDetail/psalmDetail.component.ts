import { Component, OnInit, Input } from '@angular/core';
import { Router, ActivatedRoute, NavigationEnd } from '@angular/router';

import { Psalm } from '@app/psalm/model/psalm';
import { PsalmJsonService } from '@app/psalm/service/psalmJson.service';

@Component( {
    selector: 'psalmDetail',
    templateUrl: './psalmDetail.component.html'
} )
export class PsalmDetailComponent implements OnInit {
    @Input() psalm: Psalm;

    constructor(
        private psalmJsonService: PsalmJsonService,
        private activatedRoute: ActivatedRoute,
        private router: Router
    ) { }

    ngOnInit(): void {
        this.activatedRoute.params.subscribe(params => {
            this.initPage();
        });
    }
    
    initPage() {
        let id = this.activatedRoute.snapshot.paramMap.get( "id" );
        this.psalm = this.psalmJsonService.getById( id );
        window.scroll(0,0);
        console.log( 'detail this.psalm:', this.psalm );
    }
}
