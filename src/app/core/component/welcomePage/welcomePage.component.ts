import { Component, OnInit } from '@angular/core';
import { ColorPickerModule } from 'primeng/colorpicker';
import { FormsModule } from '@angular/forms';

@Component( {
    selector: 'welcomePage',
    templateUrl: './welcomePage.component.html'
} )

export class WelcomePageComponent implements OnInit {

    constructor( ) { }
    
    ngOnInit() {
    }
}

