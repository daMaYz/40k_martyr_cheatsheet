import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { Psalm } from '@app/psalm/model/psalm';

@Component( {
    selector: 'psalmContainer',
    templateUrl: './psalmContainer.component.html'
} )
export class PsalmContainerComponent implements OnInit {
    @Input() psalm: Psalm;

    constructor() { }

    ngOnInit(): void {
    }
}
