import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegmComponent } from './regm.component';

describe('RegmComponent', () => {
  let component: RegmComponent;
  let fixture: ComponentFixture<RegmComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegmComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RegmComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
