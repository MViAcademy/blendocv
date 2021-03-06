/*
 * $Id: KX_PhysicsEngineEnums.h 35063 2011-02-22 10:33:14Z jesterking $
 *
 * ***** BEGIN GPL LICENSE BLOCK *****
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * The Original Code is Copyright (C) 2001-2002 by NaN Holding BV.
 * All rights reserved.
 *
 * The Original Code is: all of this file.
 *
 * Contributor(s): none yet.
 *
 * ***** END GPL LICENSE BLOCK *****
 */

/** \file KX_PhysicsEngineEnums.h
 *  \ingroup ketsji
 */

#ifndef __KX_PHYSICSENGINEENUMS
#define __KX_PHYSICSENGINEENUMS

enum	e_PhysicsEngine
{
		NoSelection = -1,
		UseNone     =  0,
		UseEnji     =  1,
		UseSumo     =  2,
		UseDynamo   =  3,
		UseODE      =  4,
		UseBullet	=	5,
};

#endif //__KX_PHYSICSENGINEENUMS

