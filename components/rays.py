import components.helper as helper, Constants
from objects.player import Player


class Rays(object):
    @staticmethod
    def getRaysCoordinates(player, nb_rays):
        rays = list()
        for i in range(nb_rays):
            angle = i * 180 / nb_rays - 90 + 90 / nb_rays

            if isinstance(player, Player):
                x = player.pos.x + player.width / 2
                y = player.pos.y + player.height / 2
            else:
                x = player["x"] + player["width"] / 2
                y = player["y"] + player["height"] / 2

            lineFrom = (x, y)
            lineTo = helper.getPointAtAngle(x, y, angle, 1000)
            lineWeight = 5

            rays.append((lineFrom, lineTo, lineWeight))

        return rays

    @staticmethod
    def getRaysClosestIntersection(rays, platforms):

        closest_intersections = list()

        for ray in rays:
            all_intersections_of_lines = list()
            lineFrom = ray[0]
            lineTo = ray[1]

            # compute intersection between ray and screen so that we always have an intersection
            intersections = helper.getIntersections(
                ray[0],
                ray[1],
                0,
                0,
                Constants.screenWidth,
                Constants.screenHeight,
            )
            all_intersections_of_lines.extend(intersections)

            # draw intersection
            for platform in platforms.values():
                # compute intersection between ray and platform

                intersections = helper.getIntersections(
                    lineFrom,
                    lineTo,
                    platform["x"],
                    platform["y"],
                    platform["width"],
                    platform["height"],
                )
                all_intersections_of_lines.extend(intersections)

            intersections_distances = list()
            # find closest intersection
            for intersection in all_intersections_of_lines:
                distance = helper.getNormalisedDistance(
                    lineFrom[0], lineFrom[1], intersection[0], intersection[1]
                )
                intersections_distances.append((distance, intersection))

            if len(intersections_distances) > 0:
                closest_intersection = min(intersections_distances, key=lambda t: t[0])
                closest_intersections.append(closest_intersection)

        return closest_intersections
